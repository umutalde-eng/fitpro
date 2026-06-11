// ─── Modal helpers ─────────────────────────────────────────────────────────────
function openModal(id) {
  document.getElementById(id).classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}
function closeModal(id) {
  document.getElementById(id).classList.add('hidden');
  document.body.style.overflow = '';
}
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    document.querySelectorAll('.modal:not(.hidden)').forEach(m => closeModal(m.id));
  }
});

// ─── Nav toggle ────────────────────────────────────────────────────────────────
function toggleMenu() {
  const links = document.getElementById('navLinks');
  const toggle = document.getElementById('navToggle');
  links.classList.toggle('open');
  toggle.classList.toggle('open');
}
function closeMenu() {
  const links = document.getElementById('navLinks');
  const toggle = document.getElementById('navToggle');
  if (links) links.classList.remove('open');
  if (toggle) toggle.classList.remove('open');
}
// Fermer le menu si on clique en dehors
document.addEventListener('click', function(e) {
  const nav = document.querySelector('.navbar');
  if (nav && !nav.contains(e.target)) closeMenu();
});

// ─── Login ─────────────────────────────────────────────────────────────────────
async function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;
  const errDiv = document.getElementById('loginError');

  const r = await fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  const data = await r.json();

  if (data.success) {
    window.location.href = '/dashboard';
  } else {
    errDiv.textContent = data.error;
    errDiv.classList.remove('hidden');
  }
}

// ─── Logout ────────────────────────────────────────────────────────────────────
async function logout() {
  await fetch('/api/logout', { method: 'POST' });
  window.location.href = '/';
}

// ─── Toast notifications ───────────────────────────────────────────────────────
function showToast(message, type = 'success') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.textContent = message;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(20px)';
    toast.style.transition = 'all .3s';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// ─── Lien actif dans la navbar ──────────────────────────────────────────────────
document.querySelectorAll('.nav-link').forEach(link => {
  if (link.getAttribute('href') === window.location.pathname) link.classList.add('active');
});

// ─── Success param ──────────────────────────────────────────────────────────────
const params = new URLSearchParams(window.location.search);
if (params.get('success') === '1') {
  showToast('Paiement réussi ! Bienvenue en Premium 🎉', 'success');
  history.replaceState(null, '', window.location.pathname);
}
