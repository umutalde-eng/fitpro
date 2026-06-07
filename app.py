import os
import json
import hashlib
import secrets
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import stripe

# Load .env file in development
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", secrets.token_hex(32))

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_PRICE_ID = os.environ.get("STRIPE_PRICE_ID", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
APP_URL = os.environ.get("APP_URL", "http://localhost:5001")

# ─── File-based DB — uses /data (Railway volume) or local data/ ───────────────
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(__file__), "data"))
USERS_FILE = os.path.join(DATA_DIR, "users.json")
os.makedirs(DATA_DIR, exist_ok=True)

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE) as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ─── Auth helpers ──────────────────────────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_email" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated

def get_current_user():
    if "user_email" not in session:
        return None
    users = load_users()
    return users.get(session["user_email"])

# ─── Routes ───────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    user = get_current_user()
    if user:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/onboarding")
def onboarding():
    return render_template("onboarding.html")

@app.route("/dashboard")
@login_required
def dashboard():
    user = get_current_user()
    return render_template("dashboard.html", user=user)

@app.route("/program")
@login_required
def program():
    user = get_current_user()
    if not user.get("profile"):
        return redirect(url_for("onboarding"))
    return render_template("program.html", user=user)

@app.route("/nutrition")
@login_required
def nutrition():
    user = get_current_user()
    if not user.get("profile"):
        return redirect(url_for("onboarding"))
    return render_template("nutrition.html", user=user)

@app.route("/progress")
@login_required
def progress():
    user = get_current_user()
    return render_template("progress.html", user=user)

@app.route("/pricing")
def pricing():
    user = get_current_user()
    return render_template("pricing.html", user=user)

@app.route("/coaches")
@login_required
def coaches():
    user = get_current_user()
    return render_template("coaches.html", user=user)

@app.route("/api/select-coach", methods=["POST"])
@login_required
def select_coach():
    data = request.json
    coach_id = data.get("coach_id")
    if coach_id not in ["marcus", "sarah", "karim"]:
        return jsonify({"error": "Coach invalide"}), 400
    users = load_users()
    email = session["user_email"]
    users[email]["selected_coach"] = coach_id
    save_users(users)
    return jsonify({"success": True, "coach_id": coach_id})

# ─── API ──────────────────────────────────────────────────────────────────────
@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email", "").lower().strip()
    password = data.get("password", "")
    name = data.get("name", "").strip()

    if not email or not password or not name:
        return jsonify({"error": "Tous les champs sont requis"}), 400
    if len(password) < 6:
        return jsonify({"error": "Mot de passe trop court (6 caractères min)"}), 400

    users = load_users()
    if email in users:
        return jsonify({"error": "Cet email est déjà utilisé"}), 400

    users[email] = {
        "email": email,
        "name": name,
        "password": hash_password(password),
        "created_at": datetime.now().isoformat(),
        "subscription": "free",
        "stripe_customer_id": None,
        "stripe_subscription_id": None,
        "profile": None,
        "program": None,
        "progress": [],
        "sessions_done": []
    }
    save_users(users)
    session["user_email"] = email
    return jsonify({"success": True, "name": name})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email", "").lower().strip()
    password = data.get("password", "")

    users = load_users()
    user = users.get(email)
    if not user or user["password"] != hash_password(password):
        return jsonify({"error": "Email ou mot de passe incorrect"}), 401

    session["user_email"] = email
    return jsonify({"success": True, "name": user["name"], "has_profile": bool(user.get("profile"))})

@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True})

@app.route("/api/save-profile", methods=["POST"])
@login_required
def save_profile():
    from data.programs import get_program
    data = request.json
    users = load_users()
    email = session["user_email"]

    profile = {
        "goal": data.get("goal"),
        "gender": data.get("gender"),
        "age": data.get("age"),
        "weight": data.get("weight"),
        "height": data.get("height"),
        "level": data.get("level"),
        "equipment": data.get("equipment"),
        "days_per_week": data.get("days_per_week"),
        "limitations": data.get("limitations", ""),
        "completed_at": datetime.now().isoformat()
    }

    program = get_program(profile["goal"], profile["equipment"], profile["level"])
    users[email]["profile"] = profile
    users[email]["program"] = program
    save_users(users)

    return jsonify({"success": True, "has_premium": users[email]["subscription"] == "premium"})

@app.route("/api/get-program")
@login_required
def get_program_api():
    user = get_current_user()
    if not user or not user.get("program"):
        return jsonify({"error": "Aucun programme"}), 404
    is_premium = user.get("subscription") == "premium"
    program = user["program"]

    if not is_premium:
        # Free users see week 1 only
        limited = dict(program["workout"])
        limited["weeks"] = program["workout"]["weeks"][:1]
        return jsonify({
            "workout": limited,
            "nutrition": program["nutrition"],
            "is_premium": False,
            "locked_weeks": len(program["workout"]["weeks"]) - 1
        })

    return jsonify({**program, "is_premium": True})

@app.route("/api/log-session", methods=["POST"])
@login_required
def log_session():
    data = request.json
    users = load_users()
    email = session["user_email"]
    entry = {
        "date": datetime.now().isoformat(),
        "week": data.get("week"),
        "day": data.get("day"),
        "type": data.get("type"),
        "completed": data.get("completed", True)
    }
    users[email]["sessions_done"].append(entry)
    save_users(users)
    return jsonify({"success": True})

@app.route("/api/save-progress", methods=["POST"])
@login_required
def save_progress():
    data = request.json
    users = load_users()
    email = session["user_email"]
    entry = {
        "date": datetime.now().isoformat(),
        "weight": data.get("weight"),
        "note": data.get("note", ""),
        "photos": []
    }
    users[email]["progress"].append(entry)
    save_users(users)
    return jsonify({"success": True})

@app.route("/api/get-stats")
@login_required
def get_stats():
    user = get_current_user()
    sessions = user.get("sessions_done", [])
    progress = user.get("progress", [])

    total_sessions = len([s for s in sessions if s.get("completed")])
    streak = 0
    if sessions:
        sessions_sorted = sorted(sessions, key=lambda x: x["date"], reverse=True)
        last_date = datetime.fromisoformat(sessions_sorted[0]["date"]).date()
        today = datetime.now().date()
        if (today - last_date).days <= 1:
            streak = 1
            for i in range(1, len(sessions_sorted)):
                curr = datetime.fromisoformat(sessions_sorted[i]["date"]).date()
                prev = datetime.fromisoformat(sessions_sorted[i-1]["date"]).date()
                if (prev - curr).days <= 1:
                    streak += 1
                else:
                    break

    weight_loss = 0
    if len(progress) >= 2:
        first_w = progress[0].get("weight", 0)
        last_w = progress[-1].get("weight", 0)
        if first_w and last_w:
            weight_loss = round(float(first_w) - float(last_w), 1)

    return jsonify({
        "total_sessions": total_sessions,
        "streak": streak,
        "weight_change": weight_loss,
        "progress_entries": len(progress),
        "current_week": min((total_sessions // 3) + 1, 4)
    })

# ─── Stripe ───────────────────────────────────────────────────────────────────
@app.route("/api/create-checkout", methods=["POST"])
@login_required
def create_checkout():
    if not stripe.api_key:
        return jsonify({"error": "Stripe non configuré"}), 500

    user = get_current_user()
    users = load_users()
    email = session["user_email"]

    try:
        if not user.get("stripe_customer_id"):
            customer = stripe.Customer.create(email=email, name=user["name"])
            users[email]["stripe_customer_id"] = customer.id
            save_users(users)
            customer_id = customer.id
        else:
            customer_id = user["stripe_customer_id"]

        checkout = stripe.checkout.Session.create(
            customer=customer_id,
            payment_method_types=["card"],
            line_items=[{"price": STRIPE_PRICE_ID, "quantity": 1}],
            mode="subscription",
            success_url=f"{APP_URL}/dashboard?success=1",
            cancel_url=f"{APP_URL}/pricing",
        )
        return jsonify({"url": checkout.url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/stripe-webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)
    except Exception:
        return "", 400

    if event["type"] == "checkout.session.completed":
        session_obj = event["data"]["object"]
        customer_id = session_obj.get("customer")
        sub_id = session_obj.get("subscription")
        users = load_users()
        for email, user in users.items():
            if user.get("stripe_customer_id") == customer_id:
                users[email]["subscription"] = "premium"
                users[email]["stripe_subscription_id"] = sub_id
                save_users(users)
                break

    elif event["type"] in ("customer.subscription.deleted", "customer.subscription.paused"):
        sub = event["data"]["object"]
        customer_id = sub.get("customer")
        users = load_users()
        for email, user in users.items():
            if user.get("stripe_customer_id") == customer_id:
                users[email]["subscription"] = "free"
                save_users(users)
                break

    return "", 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)
