"""
Pre-written 4-week fitness programs based on user profile.
"""

# ─── WORKOUT TEMPLATES ────────────────────────────────────────────────────────

WORKOUTS = {
    "perte_poids_maison": {
        "name": "Perte de poids – Maison",
        "weeks": [
            {
                "week": 1,
                "theme": "Mise en route",
                "days": [
                    {
                        "day": "Lundi",
                        "type": "Cardio + Full Body",
                        "duration": "30 min",
                        "exercises": [
                            {"name": "Jumping Jacks", "sets": 3, "reps": "30 sec", "rest": "15 sec"},
                            {"name": "Squats", "sets": 3, "reps": 12, "rest": "30 sec"},
                            {"name": "Pompes (genoux si besoin)", "sets": 3, "reps": 8, "rest": "30 sec"},
                            {"name": "Fentes alternées", "sets": 3, "reps": 10, "rest": "30 sec"},
                            {"name": "Mountain Climbers", "sets": 3, "reps": "20 sec", "rest": "20 sec"},
                            {"name": "Gainage planche", "sets": 3, "reps": "20 sec", "rest": "20 sec"},
                        ]
                    },
                    {
                        "day": "Mercredi",
                        "type": "Cardio HIIT",
                        "duration": "25 min",
                        "exercises": [
                            {"name": "Burpees", "sets": 4, "reps": 5, "rest": "30 sec"},
                            {"name": "High Knees", "sets": 4, "reps": "30 sec", "rest": "20 sec"},
                            {"name": "Squats Sautés", "sets": 4, "reps": 10, "rest": "30 sec"},
                            {"name": "Planche latérale", "sets": 3, "reps": "15 sec chaque côté", "rest": "20 sec"},
                        ]
                    },
                    {
                        "day": "Vendredi",
                        "type": "Full Body Renforcement",
                        "duration": "35 min",
                        "exercises": [
                            {"name": "Squats sumo", "sets": 3, "reps": 15, "rest": "30 sec"},
                            {"name": "Pompes classiques", "sets": 3, "reps": 10, "rest": "30 sec"},
                            {"name": "Hip Thrust au sol", "sets": 3, "reps": 15, "rest": "30 sec"},
                            {"name": "Dips sur chaise", "sets": 3, "reps": 10, "rest": "30 sec"},
                            {"name": "Crunchs", "sets": 3, "reps": 20, "rest": "20 sec"},
                            {"name": "Superman", "sets": 3, "reps": 12, "rest": "20 sec"},
                        ]
                    }
                ]
            },
            {
                "week": 2,
                "theme": "Montée en puissance",
                "days": [
                    {
                        "day": "Lundi",
                        "type": "Full Body Intensif",
                        "duration": "40 min",
                        "exercises": [
                            {"name": "Jumping Jacks", "sets": 3, "reps": "45 sec", "rest": "15 sec"},
                            {"name": "Squats", "sets": 4, "reps": 15, "rest": "30 sec"},
                            {"name": "Pompes", "sets": 4, "reps": 10, "rest": "30 sec"},
                            {"name": "Fentes marchées", "sets": 3, "reps": 12, "rest": "30 sec"},
                            {"name": "Mountain Climbers", "sets": 4, "reps": "30 sec", "rest": "20 sec"},
                            {"name": "Gainage planche", "sets": 4, "reps": "30 sec", "rest": "20 sec"},
                        ]
                    },
                    {
                        "day": "Mercredi",
                        "type": "HIIT Cardio",
                        "duration": "30 min",
                        "exercises": [
                            {"name": "Burpees", "sets": 5, "reps": 7, "rest": "30 sec"},
                            {"name": "High Knees", "sets": 5, "reps": "40 sec", "rest": "20 sec"},
                            {"name": "Box Jumps (sur une marche)", "sets": 4, "reps": 10, "rest": "30 sec"},
                            {"name": "Crunchs vélo", "sets": 4, "reps": 20, "rest": "20 sec"},
                        ]
                    },
                    {
                        "day": "Vendredi",
                        "type": "Lower + Core",
                        "duration": "40 min",
                        "exercises": [
                            {"name": "Squats bulgares", "sets": 3, "reps": 10, "rest": "40 sec"},
                            {"name": "Hip Thrust", "sets": 4, "reps": 15, "rest": "30 sec"},
                            {"name": "Relevés de jambes", "sets": 3, "reps": 15, "rest": "30 sec"},
                            {"name": "Gainage oblique", "sets": 3, "reps": "20 sec chaque côté", "rest": "20 sec"},
                            {"name": "Dead Bug", "sets": 3, "reps": 10, "rest": "30 sec"},
                        ]
                    },
                    {
                        "day": "Samedi",
                        "type": "Cardio Actif",
                        "duration": "30 min",
                        "exercises": [
                            {"name": "Marche rapide ou jogging", "sets": 1, "reps": "30 min continu", "rest": "-"},
                        ]
                    }
                ]
            },
            {
                "week": 3,
                "theme": "Progression",
                "days": [
                    {
                        "day": "Lundi",
                        "type": "Upper Body + Core",
                        "duration": "40 min",
                        "exercises": [
                            {"name": "Pompes larges", "sets": 4, "reps": 12, "rest": "30 sec"},
                            {"name": "Pompes serrées (triceps)", "sets": 4, "reps": 10, "rest": "30 sec"},
                            {"name": "Dips chaise", "sets": 3, "reps": 12, "rest": "30 sec"},
                            {"name": "Planche", "sets": 4, "reps": "40 sec", "rest": "20 sec"},
                            {"name": "Crunchs", "sets": 4, "reps": 25, "rest": "20 sec"},
                        ]
                    },
                    {
                        "day": "Mardi",
                        "type": "Lower Body",
                        "duration": "40 min",
                        "exercises": [
                            {"name": "Squats profonds", "sets": 4, "reps": 20, "rest": "30 sec"},
                            {"name": "Fentes sautées", "sets": 3, "reps": 10, "rest": "40 sec"},
                            {"name": "Glute Bridge", "sets": 4, "reps": 20, "rest": "30 sec"},
                            {"name": "Mollets debout", "sets": 4, "reps": 25, "rest": "20 sec"},
                        ]
                    },
                    {
                        "day": "Jeudi",
                        "type": "HIIT Total Body",
                        "duration": "35 min",
                        "exercises": [
                            {"name": "Burpees", "sets": 5, "reps": 8, "rest": "25 sec"},
                            {"name": "Squat jumps", "sets": 5, "reps": 12, "rest": "25 sec"},
                            {"name": "Mountain Climbers", "sets": 5, "reps": "40 sec", "rest": "20 sec"},
                            {"name": "Pompes explosives", "sets": 4, "reps": 8, "rest": "30 sec"},
                        ]
                    },
                    {
                        "day": "Samedi",
                        "type": "Cardio + Stretching",
                        "duration": "40 min",
                        "exercises": [
                            {"name": "Jogging léger", "sets": 1, "reps": "20 min", "rest": "-"},
                            {"name": "Stretching full body", "sets": 1, "reps": "20 min", "rest": "-"},
                        ]
                    }
                ]
            },
            {
                "week": 4,
                "theme": "Challenge final",
                "days": [
                    {
                        "day": "Lundi",
                        "type": "Full Body HIIT",
                        "duration": "45 min",
                        "exercises": [
                            {"name": "Échauffement", "sets": 1, "reps": "5 min", "rest": "-"},
                            {"name": "Circuit 1 : Burpees + Squats sautés + Pompes (30s chaque)", "sets": 5, "reps": "90 sec", "rest": "30 sec"},
                            {"name": "Circuit 2 : Fentes + Mountain Climbers + Planche (30s chaque)", "sets": 5, "reps": "90 sec", "rest": "30 sec"},
                        ]
                    },
                    {
                        "day": "Mercredi",
                        "type": "Défi Core",
                        "duration": "30 min",
                        "exercises": [
                            {"name": "Planche : 1 min", "sets": 4, "reps": "1 min", "rest": "20 sec"},
                            {"name": "Crunchs", "sets": 4, "reps": 30, "rest": "20 sec"},
                            {"name": "Relevés de jambes", "sets": 4, "reps": 20, "rest": "20 sec"},
                            {"name": "Russian Twist", "sets": 4, "reps": 20, "rest": "20 sec"},
                            {"name": "Dead Bug", "sets": 4, "reps": 12, "rest": "20 sec"},
                        ]
                    },
                    {
                        "day": "Vendredi",
                        "type": "Test Final – Max reps",
                        "duration": "45 min",
                        "exercises": [
                            {"name": "Pompes – max reps", "sets": 3, "reps": "max", "rest": "60 sec"},
                            {"name": "Squats – max reps 45 sec", "sets": 3, "reps": "max 45 sec", "rest": "45 sec"},
                            {"name": "Burpees – max 1 min", "sets": 3, "reps": "max 1 min", "rest": "60 sec"},
                            {"name": "Planche – tenir le plus longtemps", "sets": 3, "reps": "max", "rest": "60 sec"},
                        ]
                    }
                ]
            }
        ]
    },
    "prise_masse_maison": {
        "name": "Prise de masse – Maison",
        "weeks": [
            {
                "week": 1, "theme": "Fondations",
                "days": [
                    {
                        "day": "Lundi", "type": "Push (Pectoraux / Épaules / Triceps)", "duration": "45 min",
                        "exercises": [
                            {"name": "Pompes classiques", "sets": 4, "reps": 12, "rest": "60 sec"},
                            {"name": "Pompes larges (pecto)", "sets": 3, "reps": 12, "rest": "60 sec"},
                            {"name": "Pompes serrées (triceps)", "sets": 3, "reps": 10, "rest": "60 sec"},
                            {"name": "Dips sur chaise", "sets": 4, "reps": 10, "rest": "60 sec"},
                            {"name": "Pike Push-ups (épaules)", "sets": 3, "reps": 10, "rest": "60 sec"},
                        ]
                    },
                    {
                        "day": "Mercredi", "type": "Pull (Dos / Biceps)", "duration": "40 min",
                        "exercises": [
                            {"name": "Superman (dos)", "sets": 4, "reps": 15, "rest": "45 sec"},
                            {"name": "Rowing avec sac à dos lesté", "sets": 4, "reps": 12, "rest": "60 sec"},
                            {"name": "Curl biceps avec bouteilles d'eau", "sets": 4, "reps": 15, "rest": "45 sec"},
                            {"name": "Reverse Snow Angels", "sets": 3, "reps": 15, "rest": "45 sec"},
                        ]
                    },
                    {
                        "day": "Vendredi", "type": "Legs (Jambes / Fessiers)", "duration": "45 min",
                        "exercises": [
                            {"name": "Squats", "sets": 4, "reps": 15, "rest": "60 sec"},
                            {"name": "Fentes avant", "sets": 4, "reps": 12, "rest": "60 sec"},
                            {"name": "Hip Thrust au sol", "sets": 4, "reps": 15, "rest": "60 sec"},
                            {"name": "Soulevé de terre jambes tendues (sans poids)", "sets": 3, "reps": 12, "rest": "60 sec"},
                            {"name": "Mollets debout", "sets": 4, "reps": 20, "rest": "30 sec"},
                        ]
                    }
                ]
            },
            {
                "week": 2, "theme": "Surcharge progressive",
                "days": [
                    {
                        "day": "Lundi", "type": "Push Intensif", "duration": "50 min",
                        "exercises": [
                            {"name": "Pompes avec pause (2 sec en bas)", "sets": 4, "reps": 10, "rest": "75 sec"},
                            {"name": "Pompes déclinées (pieds sur chaise)", "sets": 4, "reps": 10, "rest": "75 sec"},
                            {"name": "Dips lents", "sets": 4, "reps": 10, "rest": "75 sec"},
                            {"name": "Élévations latérales (bouteilles)", "sets": 3, "reps": 15, "rest": "45 sec"},
                        ]
                    },
                    {
                        "day": "Mercredi", "type": "Pull Intensif", "duration": "45 min",
                        "exercises": [
                            {"name": "Tractions (si barre) ou inverted rows", "sets": 4, "reps": 8, "rest": "90 sec"},
                            {"name": "Rowing unilatéral (sac lesté)", "sets": 4, "reps": 10, "rest": "60 sec"},
                            {"name": "Curl marteau (bouteilles)", "sets": 4, "reps": 12, "rest": "45 sec"},
                            {"name": "Face pulls (élastique ou serviette)", "sets": 3, "reps": 15, "rest": "45 sec"},
                        ]
                    },
                    {
                        "day": "Jeudi", "type": "Legs Intensif", "duration": "50 min",
                        "exercises": [
                            {"name": "Squats bulgares (pied arrière sur chaise)", "sets": 4, "reps": 10, "rest": "90 sec"},
                            {"name": "Hip Thrust avec sac lesté", "sets": 4, "reps": 12, "rest": "60 sec"},
                            {"name": "Pistol squat assisté", "sets": 3, "reps": 8, "rest": "60 sec"},
                            {"name": "Mollets sautés", "sets": 4, "reps": 15, "rest": "30 sec"},
                        ]
                    },
                    {
                        "day": "Samedi", "type": "Full Body Light", "duration": "30 min",
                        "exercises": [
                            {"name": "Circuit : 10 pompes + 15 squats + 10 dips", "sets": 5, "reps": "enchaîné", "rest": "60 sec"},
                        ]
                    }
                ]
            },
            {
                "week": 3, "theme": "Volume Max",
                "days": [
                    {"day": "Lundi", "type": "Push Volume", "duration": "55 min",
                     "exercises": [
                         {"name": "Pompes : 5 séries de 15", "sets": 5, "reps": 15, "rest": "60 sec"},
                         {"name": "Dips : 5 séries de 12", "sets": 5, "reps": 12, "rest": "60 sec"},
                         {"name": "Pike push-ups : 4×12", "sets": 4, "reps": 12, "rest": "60 sec"},
                     ]},
                    {"day": "Mardi", "type": "Pull Volume", "duration": "50 min",
                     "exercises": [
                         {"name": "Tractions ou rows : 5×8", "sets": 5, "reps": 8, "rest": "90 sec"},
                         {"name": "Curls : 5×15", "sets": 5, "reps": 15, "rest": "45 sec"},
                     ]},
                    {"day": "Jeudi", "type": "Legs Volume", "duration": "55 min",
                     "exercises": [
                         {"name": "Squats : 5×20", "sets": 5, "reps": 20, "rest": "60 sec"},
                         {"name": "Hip Thrust : 5×15", "sets": 5, "reps": 15, "rest": "60 sec"},
                         {"name": "Fentes : 4×12", "sets": 4, "reps": 12, "rest": "60 sec"},
                     ]},
                    {"day": "Vendredi", "type": "Arms + Core", "duration": "40 min",
                     "exercises": [
                         {"name": "Dips : 4×15", "sets": 4, "reps": 15, "rest": "45 sec"},
                         {"name": "Curl : 4×15", "sets": 4, "reps": 15, "rest": "45 sec"},
                         {"name": "Planche : 4×1 min", "sets": 4, "reps": "1 min", "rest": "30 sec"},
                         {"name": "Crunchs : 4×25", "sets": 4, "reps": 25, "rest": "20 sec"},
                     ]}
                ]
            },
            {
                "week": 4, "theme": "Test de force",
                "days": [
                    {"day": "Lundi", "type": "Max Effort Push", "duration": "45 min",
                     "exercises": [
                         {"name": "Pompes – max reps (3 tentatives)", "sets": 3, "reps": "max", "rest": "3 min"},
                         {"name": "Dips – max reps", "sets": 3, "reps": "max", "rest": "2 min"},
                     ]},
                    {"day": "Mercredi", "type": "Max Effort Legs", "duration": "40 min",
                     "exercises": [
                         {"name": "Squats – max reps 2 min", "sets": 3, "reps": "max 2 min", "rest": "2 min"},
                         {"name": "Hip Thrust – max reps", "sets": 3, "reps": "max", "rest": "90 sec"},
                     ]},
                    {"day": "Vendredi", "type": "Bilan complet", "duration": "50 min",
                     "exercises": [
                         {"name": "Circuit final : pompes + squats + dips + planche", "sets": 5, "reps": "10 de chaque", "rest": "60 sec"},
                     ]}
                ]
            }
        ]
    },
    "tonification_maison": {
        "name": "Tonification – Maison",
        "weeks": [
            {"week": 1, "theme": "Réveil musculaire", "days": [
                {"day": "Lundi", "type": "Full Body Léger", "duration": "35 min",
                 "exercises": [
                     {"name": "Squats", "sets": 3, "reps": 15, "rest": "30 sec"},
                     {"name": "Pompes (genoux)", "sets": 3, "reps": 10, "rest": "30 sec"},
                     {"name": "Fentes", "sets": 3, "reps": 10, "rest": "30 sec"},
                     {"name": "Planche", "sets": 3, "reps": "20 sec", "rest": "20 sec"},
                 ]},
                {"day": "Mercredi", "type": "Lower Body + Cardio", "duration": "35 min",
                 "exercises": [
                     {"name": "Jumping Jacks", "sets": 3, "reps": "30 sec", "rest": "15 sec"},
                     {"name": "Squat jump", "sets": 3, "reps": 10, "rest": "30 sec"},
                     {"name": "Hip Thrust", "sets": 3, "reps": 15, "rest": "30 sec"},
                     {"name": "Crunchs", "sets": 3, "reps": 20, "rest": "20 sec"},
                 ]},
                {"day": "Vendredi", "type": "Upper Body + Core", "duration": "35 min",
                 "exercises": [
                     {"name": "Pompes", "sets": 3, "reps": 10, "rest": "30 sec"},
                     {"name": "Dips chaise", "sets": 3, "reps": 10, "rest": "30 sec"},
                     {"name": "Gainage", "sets": 3, "reps": "30 sec", "rest": "20 sec"},
                     {"name": "Russian Twist", "sets": 3, "reps": 15, "rest": "20 sec"},
                 ]}
            ]},
            {"week": 2, "theme": "Activation", "days": [
                {"day": "Lundi", "type": "Circuit Training", "duration": "40 min",
                 "exercises": [
                     {"name": "Circuit A : Squats 15 + Pompes 10 + Planche 30s (3 tours)", "sets": 3, "reps": "enchaîné", "rest": "60 sec"},
                     {"name": "Circuit B : Hip Thrust 15 + Crunchs 20 + Jumping Jacks 30s (3 tours)", "sets": 3, "reps": "enchaîné", "rest": "60 sec"},
                 ]},
                {"day": "Jeudi", "type": "Full Body Toning", "duration": "40 min",
                 "exercises": [
                     {"name": "Squats sumo", "sets": 4, "reps": 15, "rest": "30 sec"},
                     {"name": "Fentes sautées", "sets": 3, "reps": 10, "rest": "40 sec"},
                     {"name": "Pompes déclinées", "sets": 3, "reps": 10, "rest": "40 sec"},
                     {"name": "Gainage latéral", "sets": 3, "reps": "20 sec chaque", "rest": "20 sec"},
                 ]},
                {"day": "Samedi", "type": "Cardio doux", "duration": "30 min",
                 "exercises": [
                     {"name": "Marche rapide ou vélo", "sets": 1, "reps": "30 min", "rest": "-"},
                 ]}
            ]},
            {"week": 3, "theme": "Intensification", "days": [
                {"day": "Lundi", "type": "Lower Toning", "duration": "45 min",
                 "exercises": [
                     {"name": "Squats bulgares", "sets": 4, "reps": 12, "rest": "45 sec"},
                     {"name": "Hip Thrust unilatéral", "sets": 4, "reps": 12, "rest": "45 sec"},
                     {"name": "Donkey Kicks", "sets": 3, "reps": 15, "rest": "30 sec"},
                     {"name": "Pont fessier pulsé", "sets": 3, "reps": "30 sec", "rest": "20 sec"},
                 ]},
                {"day": "Mercredi", "type": "Upper Toning", "duration": "40 min",
                 "exercises": [
                     {"name": "Pompes lentes (3 sec descente)", "sets": 4, "reps": 10, "rest": "45 sec"},
                     {"name": "Dips lents", "sets": 4, "reps": 10, "rest": "45 sec"},
                     {"name": "Planche alternée", "sets": 3, "reps": "30 sec", "rest": "20 sec"},
                 ]},
                {"day": "Vendredi", "type": "HIIT Léger", "duration": "35 min",
                 "exercises": [
                     {"name": "20s effort / 10s repos × 8 rounds : Burpees", "sets": 2, "reps": "8 rounds", "rest": "60 sec"},
                     {"name": "20s effort / 10s repos × 8 rounds : Squats sautés", "sets": 2, "reps": "8 rounds", "rest": "60 sec"},
                 ]}
            ]},
            {"week": 4, "theme": "Final Toning", "days": [
                {"day": "Lundi", "type": "Full Body Challenge", "duration": "50 min",
                 "exercises": [
                     {"name": "AMRAP 20 min : 10 squats + 8 pompes + 12 hip thrust + 30s planche", "sets": 1, "reps": "20 min", "rest": "selon besoin"},
                 ]},
                {"day": "Mercredi", "type": "Core Final", "duration": "30 min",
                 "exercises": [
                     {"name": "Planche 1 min", "sets": 4, "reps": "1 min", "rest": "20 sec"},
                     {"name": "V-Sit", "sets": 4, "reps": "30 sec", "rest": "20 sec"},
                     {"name": "Dead Bug", "sets": 3, "reps": 12, "rest": "30 sec"},
                 ]},
                {"day": "Vendredi", "type": "Bilan Toning", "duration": "45 min",
                 "exercises": [
                     {"name": "Max reps pompes", "sets": 3, "reps": "max", "rest": "2 min"},
                     {"name": "Max reps squats 60 sec", "sets": 3, "reps": "max 60 sec", "rest": "2 min"},
                     {"name": "Planche max", "sets": 3, "reps": "max", "rest": "2 min"},
                 ]}
            ]}
        ]
    }
}

# ─── DETAILED WEEKLY NUTRITION PLANS ─────────────────────────────────────────

DAYS_FR = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

def make_day(calories, petit_dej, dejeuner, diner, collation, tip=""):
    return {"calories": calories, "petit_dejeuner": petit_dej, "dejeuner": dejeuner, "diner": diner, "collation": collation, "tip": tip}

NUTRITION_WEEKS = {
    "perte_poids": [
        # ── SEMAINE 1 ──────────────────────────────────────────────────────────
        {
            "week": 1, "theme": "Mise en route – Rééquilibrage",
            "intro": "Cette semaine on installe de nouvelles habitudes sans frustration. Objectif : -300 kcal/jour par rapport à ta maintenance.",
            "calories_day": "1 600 – 1 800 kcal",
            "macros": {"proteines": "130g", "glucides": "180g", "lipides": "55g"},
            "shopping_list": ["Flocons d'avoine", "Yaourt grec 0%", "Œufs x12", "Poulet (600g)", "Thon en boîte x4", "Riz complet", "Patate douce x4", "Brocolis", "Épinards", "Tomates cerises", "Concombre", "Citron", "Pommes x6", "Bananes x4", "Amandes (150g)", "Huile d'olive", "Pain complet"],
            "prep_tips": ["Cuire 400g de riz complet le dimanche pour toute la semaine", "Préparer 4 blancs de poulet grillés à l'avance", "Couper les légumes en avance et les stocker en boîte"],
            "days": [
                make_day(1650,
                    {"name": "Porridge protéiné", "detail": "60g flocons d'avoine + lait écrémé + 1 scoop protéine vanille (ou 3 blancs d'œuf) + ½ banane tranchée", "kcal": 380},
                    {"name": "Poulet riz légumes", "detail": "150g poulet grillé + 70g riz complet (cru) + brocolis vapeur + filet d'huile d'olive", "kcal": 520},
                    {"name": "Omelette aux légumes", "detail": "3 œufs + épinards + tomates + 1 tranche pain complet", "kcal": 420},
                    {"name": "1 pomme + 15g amandes", "kcal": 150}, "Boire 2L d'eau minimum aujourd'hui."),
                make_day(1680,
                    {"name": "Œufs brouillés + toast", "detail": "3 œufs brouillés + 2 tranches pain complet + café sans sucre", "kcal": 400},
                    {"name": "Salade thon-pois chiches", "detail": "1 boîte thon (140g) + 100g pois chiches égouttés + tomates cerises + concombre + vinaigrette citronnée", "kcal": 490},
                    {"name": "Soupe + dinde", "detail": "Soupe de légumes maison (courgette, carotte) + 120g blanc de dinde + 1 yaourt grec 0%", "kcal": 430},
                    {"name": "Fromage blanc 0% + 1 c. à c. miel", "kcal": 120}, "Prends 10 min de marche après le dîner."),
                make_day(1600,
                    {"name": "Yaourt grec + fruits", "detail": "200g yaourt grec 0% + 80g fruits rouges + 20g granola maison + 1 c. à c. graines de chia", "kcal": 310},
                    {"name": "Saumon quinoa", "detail": "130g saumon vapeur + 60g quinoa (cru) + épinards sautés à l'ail", "kcal": 530},
                    {"name": "Poulet patate douce", "detail": "120g poulet + 150g patate douce rôtie + salade verte", "kcal": 450},
                    {"name": "½ banane + 10 noix cajou", "kcal": 160}, "Jour de repos musculaire – marche 20 min."),
                make_day(1700,
                    {"name": "Porridge avoine-banane", "detail": "60g flocons d'avoine + 1 banane + 200ml lait végétal + cannelle", "kcal": 370},
                    {"name": "Wrap poulet-avocat", "detail": "1 tortilla complète + 130g poulet émincé + ½ avocat + salade + tomate", "kcal": 520},
                    {"name": "Lentilles corail", "detail": "80g lentilles corail (cru) + légumes poêlés (courgette, poivron) + 1 yaourt grec", "kcal": 460},
                    {"name": "1 pomme + 15g amandes", "kcal": 150}, "Séance d'entraînement ce soir – mange la collation 1h avant."),
                make_day(1750,
                    {"name": "Smoothie bowl", "detail": "Mixeur : 1 banane + 100g fruits rouges + 150ml lait végétal + 1 scoop protéine. Toppings : 15g granola + 1 c. à c. beurre cacahuète", "kcal": 420},
                    {"name": "Riz complet + œufs durs", "detail": "80g riz complet (cru) + 3 œufs durs + salade niçoise (haricots verts, tomates, olives)", "kcal": 530},
                    {"name": "Cabillaud vapeur", "detail": "150g cabillaud + légumes vapeur variés + 100g pomme de terre", "kcal": 430},
                    {"name": "200g fromage blanc 0%", "kcal": 120}, "Bonne séance ! Hydrate-toi bien après l'effort."),
                make_day(1800,
                    {"name": "Toast avocat-œufs", "detail": "2 tranches pain complet + ½ avocat écrasé + 2 œufs pochés + poivre + sel", "kcal": 450},
                    {"name": "Salade complète", "detail": "Grandes assiette : 130g poulet + 2 œufs durs + tomates, concombre, maïs, feta légère + vinaigrette légère", "kcal": 540},
                    {"name": "Dîner léger", "detail": "Soupe détox (courgette + brocoli) mixée + 2 œufs durs", "kcal": 380},
                    {"name": "1 orange + 15g noix", "kcal": 160}, "Repas plaisir autorisé ce soir si envie – reste raisonnable."),
                make_day(1600,
                    {"name": "Œufs + légumes sautés", "detail": "3 œufs + épinards + champignons sautés + café", "kcal": 360},
                    {"name": "Poulet rôti maison", "detail": "180g poulet rôti + haricots verts + carottes + 60g riz complet", "kcal": 520},
                    {"name": "Soupe maison + yaourt", "detail": "Grande soupe de légumes + 1 yaourt grec 0%", "kcal": 320},
                    {"name": "1 poignée fruits secs", "kcal": 130}, "Prépare ta liste de courses pour la semaine 2 !"),
            ]
        },
        # ── SEMAINE 2 ──────────────────────────────────────────────────────────
        {
            "week": 2, "theme": "Optimisation – Boost métabolique",
            "intro": "On intensifie le déficit légèrement et on structure mieux les repas autour des entraînements.",
            "calories_day": "1 550 – 1 750 kcal",
            "macros": {"proteines": "145g", "glucides": "165g", "lipides": "50g"},
            "shopping_list": ["Blanc de poulet (700g)", "Saumon (400g)", "Thon boîte x5", "Œufs x15", "Yaourt grec 0% x6", "Riz complet", "Quinoa", "Patate douce x5", "Brocolis", "Courgettes", "Poivrons x3", "Épinards", "Fruits rouges (surgelés ok)", "Citrons x3", "Amandes", "Noix", "Huile d'olive", "Herbes fraîches"],
            "prep_tips": ["Prépare des batch cooking : 500g riz + 600g poulet le dimanche", "Prépare 6 œufs durs pour les collations", "Mixe des smoothies la veille et garde-les au frigo"],
            "days": [
                make_day(1620,
                    {"name": "Porridge high-protéine", "detail": "50g flocons d'avoine + 200ml lait écrémé + 2 blancs d'œuf cuits dedans + ½ pomme râpée + cannelle", "kcal": 350},
                    {"name": "Bol Buddha poulet", "detail": "130g poulet grillé + 60g quinoa + avocat (¼) + concombre + carottes râpées + sauce tahini légère", "kcal": 510},
                    {"name": "Pavé de saumon", "detail": "150g saumon four + courgettes rôties + 80g patate douce", "kcal": 480},
                    {"name": "1 œuf dur + 1 pomme", "kcal": 140}, "Semaine 2 : augmente l'intensité de tes séances."),
                make_day(1580,
                    {"name": "Yaourt grec + chia + fruits", "detail": "180g yaourt grec 0% + 2 c. à c. graines de chia + 100g fruits rouges + 10g noix", "kcal": 290},
                    {"name": "Salade thon-lentilles", "detail": "1 boîte thon + 100g lentilles cuites + tomates + concombre + vinaigrette moutarde-citron", "kcal": 480},
                    {"name": "Blanc de dinde + légumes", "detail": "150g dinde + haricots verts + carottes + 1 tranche pain complet grillé", "kcal": 430},
                    {"name": "Fromage blanc 0% + 1 c. miel", "kcal": 110}, "Jour de repos : marche 30 min en journée."),
                make_day(1700,
                    {"name": "Omelette épinards-feta", "detail": "3 œufs + grosse poignée épinards + 20g feta légère + tomate + café", "kcal": 390},
                    {"name": "Riz + poulet + brocolis", "detail": "70g riz complet (cru) + 160g poulet grillé + brocolis vapeur + herbes fraîches", "kcal": 530},
                    {"name": "Soupe détox + sardines", "detail": "Grande soupe poireaux-courgettes + 1 boîte sardines à l'huile d'olive égouttées + pain seigle", "kcal": 420},
                    {"name": "15g amandes + 1 orange", "kcal": 165}, "Séance intense aujourd'hui – mange bien !"),
                make_day(1560,
                    {"name": "Pancakes avoine-banane", "detail": "40g flocons d'avoine mixés + 1 banane + 2 œufs + 1 pincée sel – cuire à sec ou huile coco", "kcal": 380},
                    {"name": "Wrap thon-avocat", "detail": "1 tortilla complète + 1 boîte thon + ½ avocat + salade + tomates + jus citron", "kcal": 480},
                    {"name": "Poulet épices + légumes", "detail": "140g poulet mariné curry + poivrons + courgettes rôtis au four", "kcal": 390},
                    {"name": "1 yaourt grec + 10g noix", "kcal": 160}, "Hydrate-toi bien : 2.5L eau minimum."),
                make_day(1750,
                    {"name": "Toast saumon fumé", "detail": "2 tranches pain complet + 60g saumon fumé + fromage frais allégé + câpres + citron", "kcal": 410},
                    {"name": "Bol quinoa complet", "detail": "70g quinoa + 130g crevettes sautées ail-citron + concombre + tomates cerises + avocat (¼)", "kcal": 520},
                    {"name": "Saumon + patate douce", "detail": "150g saumon vapeur + 140g patate douce + brocolis + citron", "kcal": 470},
                    {"name": "200g fromage blanc 0%", "kcal": 120}, "Dernier entraînement de la semaine – donne tout !"),
                make_day(1800,
                    {"name": "Œufs bénédictine light", "detail": "2 œufs pochés + 1 tranche jambon blanc dégraissé + 2 tranches pain complet + salade", "kcal": 430},
                    {"name": "Poulet rôti famille", "detail": "200g poulet rôti + ratatouille maison + 80g riz complet", "kcal": 570},
                    {"name": "Dîner léger volontaire", "detail": "Soupe miso + 150g tofu sauté + légumes verts", "kcal": 320},
                    {"name": "1 carré chocolat noir 85% + thé", "kcal": 70}, "Repas du samedi : 1 écart raisonnable autorisé."),
                make_day(1580,
                    {"name": "Porridge detox", "detail": "50g flocons d'avoine + lait végétal + 1 c. à c. graines de lin + ½ poire + cannelle", "kcal": 330},
                    {"name": "Salade composée", "detail": "Poulet froid + lentilles + carottes + épinards + vinaigrette légère", "kcal": 490},
                    {"name": "Soupe légumes + œufs", "detail": "Grande soupe de légumes maison + 2 œufs durs", "kcal": 360},
                    {"name": "1 pomme + 15g amandes", "kcal": 150}, "Dimanche doux – prépare ta semaine 3 !"),
            ]
        },
        # ── SEMAINE 3 ──────────────────────────────────────────────────────────
        {
            "week": 3, "theme": "Accélération – Fat burning",
            "intro": "Semaine clé : on pousse le déficit et on maximise les apports en protéines pour préserver le muscle.",
            "calories_day": "1 500 – 1 700 kcal",
            "macros": {"proteines": "155g", "glucides": "150g", "lipides": "48g"},
            "shopping_list": ["Blanc de poulet (800g)", "Crevettes (300g)", "Œufs x15", "Thon boîte x5", "Yaourt grec 0% x8", "Skyr nature x4", "Riz complet", "Patate douce x4", "Haricots verts", "Épinards", "Courgettes", "Champignons", "Tomates", "Citrons x4", "Fruits rouges", "Amandes", "Beurre de cacahuète naturel", "Herbes fraîches"],
            "prep_tips": ["Prépare 700g de poulet grillé en début de semaine", "Fais une grosse soupe de légumes pour 3 jours", "Prépare des portions de riz et patate douce à l'avance"],
            "days": [
                make_day(1600,
                    {"name": "Skyr + fruits + graines", "detail": "200g skyr nature + 100g fruits rouges + 1 c. à s. graines mélangées + 5g noix concassées", "kcal": 280},
                    {"name": "Poulet grillé + légumes", "detail": "170g poulet grillé épices + 60g riz complet + haricots verts + courgettes sautées", "kcal": 530},
                    {"name": "Crevettes sautées", "detail": "200g crevettes ail-citron-persil + épinards sautés + 80g patate douce", "kcal": 430},
                    {"name": "1 œuf dur + 1 pomme", "kcal": 150}, "Semaine 3 : le plus dur mais les résultats arrivent !"),
                make_day(1540,
                    {"name": "Omelette champignons", "detail": "3 œufs + 100g champignons + épinards + sel, poivre + café sans sucre", "kcal": 320},
                    {"name": "Salade niçoise", "detail": "2 boîtes thon + 3 œufs durs + haricots verts + tomates + olives noires + vinaigrette légère", "kcal": 520},
                    {"name": "Dinde + légumes vapeur", "detail": "150g blanc dinde + carottes + brocolis + poireaux vapeur + bouillon dégraissé", "kcal": 380},
                    {"name": "200g fromage blanc 0%", "kcal": 110}, "Repos – marche 30 min si possible."),
                make_day(1680,
                    {"name": "Porridge protéiné max", "detail": "50g flocons d'avoine + 2 blancs d'œuf cuits + 1 scoop protéine vanille + ½ banane + lait écrémé", "kcal": 400},
                    {"name": "Bol poulet-quinoa", "detail": "160g poulet + 60g quinoa + avocat (¼) + épinards + vinaigrette citron-herbes", "kcal": 540},
                    {"name": "Saumon + courgettes", "detail": "150g saumon papillote citron-aneth + courgettes + carottes + 80g patate douce", "kcal": 450},
                    {"name": "1 yaourt grec + 15g amandes", "kcal": 190}, "Séance HIIT ce soir – prends la collation 1h30 avant."),
                make_day(1510,
                    {"name": "Thé + œufs + toast", "detail": "2 œufs pochés + 1 tranche pain de seigle + ½ avocat + thé vert", "kcal": 350},
                    {"name": "Soupe protéinée", "detail": "Soupe lentilles-légumes maison (200ml) + 130g poulet grillé + 1 tranche pain complet", "kcal": 490},
                    {"name": "Cabillaud four", "detail": "170g cabillaud four + légumes rôtis (poivrons, courgettes, tomates) + filet d'huile d'olive", "kcal": 380},
                    {"name": "Skyr 150g + 10g graines chia", "kcal": 160}, "Jour calme – écoute ton corps."),
                make_day(1700,
                    {"name": "Smoothie bowl", "detail": "Base mixée : 1 banane + 150g fruits rouges + 150ml lait végétal. Toppings : 10g granola + 5g noix + 1 c. beurre cacahuète", "kcal": 420},
                    {"name": "Crevettes-riz", "detail": "200g crevettes sautées ail-citron + 65g riz complet + poivrons + courgettes", "kcal": 490},
                    {"name": "Poulet tikka maison", "detail": "150g poulet mariné yaourt-curcuma-garam masala + 100g riz complet + salade verte", "kcal": 490},
                    {"name": "1 carré chocolat 85% + tisane", "kcal": 60}, "Vendredi – tu as assuré cette semaine, bravo !"),
                make_day(1750,
                    {"name": "Brunch léger", "detail": "3 œufs brouillés + 2 tranches pain complet + tomates + fromage frais 0%", "kcal": 430},
                    {"name": "Repas plaisir raisonnable", "detail": "Mange ce que tu aimes mais en contrôlant les portions – max 650 kcal", "kcal": 650},
                    {"name": "Dîner détox", "detail": "Grande soupe de légumes sans féculents + 1 yaourt grec 0%", "kcal": 280},
                    {"name": "Fruits frais", "kcal": 100}, "1 repas plaisir par semaine – c'est important pour tenir !"),
                make_day(1550,
                    {"name": "Œufs + légumes", "detail": "3 œufs + épinards + poivrons sautés + café noir", "kcal": 330},
                    {"name": "Salade poulet-légumes", "detail": "150g poulet froid + salade verte + tomates + concombre + vinaigrette légère", "kcal": 440},
                    {"name": "Soupe + skyr", "detail": "Soupe courgettes-brocolis mixée + 200g skyr nature + 10g noix", "kcal": 360},
                    {"name": "1 pomme + 10g amandes", "kcal": 130}, "Dimanche récupération – préparation semaine 4 !"),
            ]
        },
        # ── SEMAINE 4 ──────────────────────────────────────────────────────────
        {
            "week": 4, "theme": "Sprint final – Résultats visibles",
            "intro": "Dernière semaine ! On maintient le déficit tout en assurant l'énergie pour les séances finales.",
            "calories_day": "1 500 – 1 700 kcal",
            "macros": {"proteines": "160g", "glucides": "145g", "lipides": "48g"},
            "shopping_list": ["Blanc de poulet (900g)", "Saumon (400g)", "Crevettes (300g)", "Œufs x18", "Yaourt grec 0% x8", "Skyr x4", "Patate douce x4", "Riz complet", "Quinoa", "Épinards", "Brocolis", "Asperges", "Haricots verts", "Tomates cerises", "Citrons x5", "Avocats x3", "Amandes", "Baies de goji"],
            "prep_tips": ["Batch cooking max ce dimanche", "Prépare 8 portions repas pour la semaine", "Pèse tes aliments cette semaine pour voir tes progrès"],
            "days": [
                make_day(1620,
                    {"name": "Porridge final", "detail": "50g flocons d'avoine + 200ml lait écrémé + 1 scoop protéine + ½ banane + baies de goji", "kcal": 380},
                    {"name": "Chicken bowl", "detail": "170g poulet grillé + 60g quinoa + avocat (¼) + épinards + tomates cerises + citron", "kcal": 530},
                    {"name": "Saumon asperges", "detail": "160g saumon four + asperges rôties + 80g patate douce + citron", "kcal": 450},
                    {"name": "1 œuf dur + skyr 100g", "kcal": 155}, "Semaine 4 – la ligne d'arrivée est proche !"),
                make_day(1570,
                    {"name": "Omelette complète", "detail": "3 œufs + épinards + tomates + 20g feta + café", "kcal": 370},
                    {"name": "Salade suprême", "detail": "150g crevettes + 100g pois chiches + tomates cerises + concombre + avocat + vinaigrette citronnée", "kcal": 510},
                    {"name": "Dinde vapeur", "detail": "150g dinde vapeur + haricots verts + carottes + bouillon d'herbes", "kcal": 370},
                    {"name": "200g fromage blanc 0% + 1 c. miel", "kcal": 130}, "2 jours avant la fin – mental fort !"),
                make_day(1700,
                    {"name": "Toast protéiné", "detail": "2 tranches pain de seigle + 2 œufs pochés + ½ avocat + saumon fumé 30g", "kcal": 430},
                    {"name": "Riz poulet power", "detail": "70g riz complet + 170g poulet + brocolis + courgettes + sauce soja légère", "kcal": 530},
                    {"name": "Pavé saumon complet", "detail": "160g saumon + lentilles vertes 80g cuit + épinards + citron", "kcal": 480},
                    {"name": "1 yaourt grec + amandes", "kcal": 190}, "Avant-dernière séance – donne tout !"),
                make_day(1530,
                    {"name": "Skyr bowl", "detail": "200g skyr + 100g fruits rouges + 10g graines chia + 10g noix + filet miel", "kcal": 310},
                    {"name": "Wrap complet", "detail": "1 tortilla complète + 140g poulet + salade + tomate + ½ avocat + fromage frais 0%", "kcal": 490},
                    {"name": "Soupe protéinée finale", "detail": "Soupe lentilles-légumes + 1 œuf poché + pain de seigle", "kcal": 420},
                    {"name": "1 pomme + 10g amandes", "kcal": 130}, "Calme avant la tempête – séance finale demain !"),
                make_day(1750,
                    {"name": "Petit-déj champion", "detail": "3 œufs brouillés + 2 tranches pain complet + ½ avocat + tomates + jus citron", "kcal": 460},
                    {"name": "Bol power final", "detail": "170g poulet + 70g quinoa + avocat + légumes grillés + sauce tahini light", "kcal": 550},
                    {"name": "Saumon cérémonie", "detail": "160g saumon four + asperges + patate douce + herbes fraîches", "kcal": 450},
                    {"name": "Fruits + chocolat 85%", "kcal": 120}, "DERNIÈRE SÉANCE – felicitations, tu as tout donné !"),
                make_day(1800,
                    {"name": "Brunch célébration", "detail": "Ce que tu veux mais équilibré – tu mérites un bon repas !", "kcal": 500},
                    {"name": "Repas plaisir mérité", "detail": "Repas plaisir – tu as terminé 4 semaines, félicitations !", "kcal": 700},
                    {"name": "Dîner léger", "detail": "Soupe légumes + yaourt grec", "kcal": 280},
                    {"name": "Thé ou tisane", "kcal": 0}, "TU AS RÉUSSI LES 4 SEMAINES ! Bilan lundi matin."),
                make_day(1600,
                    {"name": "Petit-déj habituel", "detail": "Porridge ou œufs selon envie", "kcal": 380},
                    {"name": "Repas équilibré", "detail": "Poulet + légumes + féculents", "kcal": 520},
                    {"name": "Dîner léger", "detail": "Soupe + protéine légère", "kcal": 380},
                    {"name": "Collation légère", "kcal": 130}, "Continue ces habitudes – elles sont maintenant les tiennes !"),
            ]
        }
    ],

    "prise_masse": [
        {
            "week": 1, "theme": "Fondations caloriques",
            "intro": "Semaine 1 : installer un surplus calorique de qualité. Chaque repas compte pour construire du muscle.",
            "calories_day": "2 800 – 3 100 kcal",
            "macros": {"proteines": "165g", "glucides": "360g", "lipides": "85g"},
            "shopping_list": ["Blanc de poulet (1kg)", "Steak haché 5% (600g)", "Œufs x18", "Lait entier (2L)", "Fromage blanc", "Riz blanc (1kg)", "Pâtes complètes (500g)", "Patate douce x6", "Bananes x8", "Flocons d'avoine (800g)", "Beurre de cacahuète", "Amandes (200g)", "Avocats x4", "Brocolis", "Épinards", "Huile d'olive"],
            "prep_tips": ["Cuire 1kg de riz le dimanche", "Préparer 800g de poulet grillé", "Avoir toujours des œufs durs prêts", "Peser tes portions les 3 premiers jours"],
            "days": [
                make_day(2900,
                    {"name": "Petit-déj masse", "detail": "80g flocons d'avoine + 300ml lait entier + 3 œufs brouillés + 1 banane + 1 c. à s. beurre cacahuète", "kcal": 720},
                    {"name": "Riz-poulet-légumes", "detail": "120g riz blanc (cru) + 200g poulet grillé + brocolis + 1 c. à s. huile d'olive", "kcal": 780},
                    {"name": "Pâtes steak haché", "detail": "100g pâtes (cru) + 150g steak haché 5% + sauce tomate maison + parmesan léger", "kcal": 720},
                    {"name": "Shaker + banane", "detail": "30g whey protéine + 300ml lait entier + 1 banane + 30g flocons d'avoine", "kcal": 540}, "Post-workout ou avant coucher."),
                make_day(2850,
                    {"name": "Pancakes mass-builder", "detail": "3 œufs + 60g flocons d'avoine mixés + 1 banane + 200ml lait + sirop d'érable – 6 pancakes", "kcal": 680},
                    {"name": "Riz + thon + avocat", "detail": "110g riz + 2 boîtes thon + 1 avocat + maïs + vinaigrette huile d'olive", "kcal": 730},
                    {"name": "Poulet patate douce", "detail": "200g poulet + 250g patate douce + haricots verts + 2 c. à s. huile olive", "kcal": 680},
                    {"name": "Fromage blanc + noix + miel", "detail": "300g fromage blanc + 40g noix + 1 c. à s. miel", "kcal": 520}, "Repos – mange bien malgré l'absence de séance."),
                make_day(3000,
                    {"name": "Breakfast champion", "detail": "4 œufs brouillés + 80g flocons d'avoine + 300ml lait + 2 tranches pain complet + ½ avocat", "kcal": 780},
                    {"name": "Poulet riz légumes", "detail": "200g poulet + 120g riz + légumes verts + 2 c. s. huile olive", "kcal": 780},
                    {"name": "Saumon pâtes", "detail": "180g saumon + 100g pâtes (cru) + épinards + crème légère", "kcal": 720},
                    {"name": "Shaker double", "detail": "40g whey + 400ml lait + 1 banane + 20g beurre cacahuète", "kcal": 620}, "Séance – mange le shaker 1h30 après."),
                make_day(2800,
                    {"name": "Avoine-œufs-banane", "detail": "70g flocons d'avoine + 3 œufs + 1 banane + lait entier 200ml", "kcal": 700},
                    {"name": "Riz complet + bœuf", "detail": "100g riz complet + 170g bœuf haché 5% + courgettes + tomates", "kcal": 720},
                    {"name": "Blanc dinde + pomme de terre", "detail": "200g dinde + 250g pommes de terre vapeur + haricots verts + huile olive", "kcal": 680},
                    {"name": "Yaourt grec + fruits", "detail": "300g yaourt grec entier + 1 banane + 20g amandes", "kcal": 450}, ""),
                make_day(3100,
                    {"name": "Gros petit-déj", "detail": "4 œufs + 3 tranches pain complet + 1 c. à s. beurre cacahuète + 1 banane + lait entier", "kcal": 820},
                    {"name": "Poulet riz avocat", "detail": "210g poulet + 120g riz + 1 avocat + salade + vinaigrette huile olive", "kcal": 800},
                    {"name": "Steak haché pâtes", "detail": "170g steak haché + 100g pâtes + sauce bolognaise maison + parmesan", "kcal": 760},
                    {"name": "Mass gainer maison", "detail": "50g flocons d'avoine + 40g whey + 400ml lait + 1 banane + 1 c. beurre cacahuète", "kcal": 680}, "Grande séance – tu as besoin de carburant !"),
                make_day(3000,
                    {"name": "Brunch dominical", "detail": "4 œufs brouillés + 3 tranches pain complet + 1 avocat + saumon fumé 60g", "kcal": 750},
                    {"name": "Repas convivial", "detail": "Mange avec plaisir – poulet/viande + féculents + légumes + dessert fruité", "kcal": 850},
                    {"name": "Dîner constructeur", "detail": "180g saumon + 100g riz + brocolis + épinards", "kcal": 650},
                    {"name": "Shaker nuit", "detail": "40g whey + 300ml lait entier", "kcal": 400}, "Samedi plaisir – mange bien et profite."),
                make_day(2850,
                    {"name": "Porridge classique", "detail": "80g flocons d'avoine + lait + 1 banane + œufs", "kcal": 700},
                    {"name": "Riz + poulet batch", "detail": "Le batch de la semaine + légumes frais", "kcal": 750},
                    {"name": "Porc + patate douce", "detail": "180g porc maigre + 200g patate douce + légumes", "kcal": 660},
                    {"name": "Lait + noix", "detail": "350ml lait entier + 30g noix", "kcal": 350}, "Prépare ta semaine 2 – batch cook !"),
            ]
        },
        {
            "week": 2, "theme": "Surcharge progressive",
            "intro": "Augmente légèrement les glucides autour des séances. Le muscle se construit aussi à table.",
            "calories_day": "2 950 – 3 200 kcal",
            "macros": {"proteines": "175g", "glucides": "390g", "lipides": "88g"},
            "shopping_list": ["Poulet (1.2kg)", "Saumon (500g)", "Steak haché 5% (500g)", "Œufs x20", "Lait entier (2L)", "Whey protéine", "Riz blanc (1kg)", "Pâtes (500g)", "Pommes de terre (1kg)", "Avocats x5", "Bananes x10", "Flocons d'avoine (800g)", "Fromage blanc", "Yaourt grec entier x6", "Légumes variés"],
            "prep_tips": ["Augmente les portions de 10-15%", "Mange dans les 30 min post-séance", "Prépare un mass gainer maison quotidien"],
            "days": [
                make_day(3000,
                    {"name": "Petit-déj énergie+", "detail": "90g flocons d'avoine + 350ml lait entier + 3 œufs + 1 banane + 1.5 c. beurre cacahuète", "kcal": 800},
                    {"name": "Riz-poulet power", "detail": "130g riz blanc + 220g poulet + légumes verts + 2 c. huile olive + sauce soja", "kcal": 830},
                    {"name": "Pâtes bolognaise", "detail": "110g pâtes + 160g bœuf haché + sauce tomate + parmesan 15g", "kcal": 750},
                    {"name": "Shaker post-workout", "detail": "40g whey + 400ml lait + 1 banane + 30g flocons d'avoine", "kcal": 620}, ""),
                make_day(2950,
                    {"name": "Pancakes XXL", "detail": "3 œufs + 80g flocons d'avoine + 250ml lait + banane + sirop érable – 7 pancakes", "kcal": 780},
                    {"name": "Bol complet", "detail": "110g riz + 200g saumon + avocat + épinards + graines sésame + tamari", "kcal": 820},
                    {"name": "Poulet pomme de terre", "detail": "200g poulet + 280g pommes de terre vapeur + haricots + huile olive", "kcal": 720},
                    {"name": "Fromage blanc + miel + noix", "detail": "300g fromage blanc + 40g noix + 2 c. miel", "kcal": 550}, ""),
                make_day(3100,
                    {"name": "Gros déj champion", "detail": "4 œufs + 3 tranches pain + 1 avocat + banane + lait entier", "kcal": 820},
                    {"name": "Poulet riz max", "detail": "230g poulet + 130g riz + brocolis + courgettes + huile olive", "kcal": 850},
                    {"name": "Saumon pâtes crème", "detail": "180g saumon + 110g pâtes + épinards + fromage frais 15% 50g", "kcal": 760},
                    {"name": "Mass gainer maison", "detail": "50g flocons + 40g whey + 400ml lait + banane + beurre cacahuète", "kcal": 680}, "Séance intense aujourd'hui."),
                make_day(2900,
                    {"name": "Avoine œufs banane", "detail": "80g flocons + 3 œufs + banane + 300ml lait", "kcal": 730},
                    {"name": "Bœuf riz légumes", "detail": "170g bœuf haché + 110g riz + légumes + 2 c. huile olive", "kcal": 780},
                    {"name": "Dinde + patate douce", "detail": "200g dinde + 250g patate douce + épinards", "kcal": 680},
                    {"name": "Yaourt grec entier + fruits", "detail": "300g + 1 banane + amandes", "kcal": 470}, ""),
                make_day(3200,
                    {"name": "Breakfast final", "detail": "4 œufs + 90g flocons + 350ml lait + banane + 2 c. beurre cacahuète", "kcal": 870},
                    {"name": "Poulet riz avocat", "detail": "230g poulet + 130g riz + 1 avocat + salade", "kcal": 840},
                    {"name": "Steak patates", "detail": "200g steak + 280g pommes de terre + haricots verts + huile olive", "kcal": 800},
                    {"name": "Shaker nuit", "detail": "50g whey + 400ml lait + banane + 30g flocons", "kcal": 680}, "Grande séance semaine 2."),
                make_day(3050,
                    {"name": "Brunch mass", "detail": "4 œufs + 3 tranches pain + beurre cacahuète + banane + lait", "kcal": 780},
                    {"name": "Repas social", "detail": "Mange librement dans un contexte sain – viande + féculents + légumes", "kcal": 900},
                    {"name": "Saumon épinards", "detail": "180g saumon + épinards + riz complet 90g", "kcal": 620},
                    {"name": "Shaker classique", "detail": "40g whey + 300ml lait entier", "kcal": 380}, ""),
                make_day(2900,
                    {"name": "Porridge dominical", "detail": "90g flocons + lait + banane + œufs brouillés", "kcal": 740},
                    {"name": "Riz poulet batch S3", "detail": "Prépare les repas de semaine 3", "kcal": 800},
                    {"name": "Porc + légumes + patate", "detail": "180g porc + patate douce + légumes", "kcal": 660},
                    {"name": "Lait + amandes + banane", "kcal": 420}, "Prépare ta semaine 3 – batch cook !"),
            ]
        },
        {
            "week": 3, "theme": "Volume Maximum",
            "intro": "Semaine volume : on pousse les calories au maximum pour maximiser la croissance musculaire.",
            "calories_day": "3 100 – 3 400 kcal",
            "macros": {"proteines": "185g", "glucides": "420g", "lipides": "92g"},
            "shopping_list": ["Poulet (1.5kg)", "Saumon (500g)", "Bœuf haché 5% (600g)", "Œufs x24", "Lait entier (3L)", "Whey protéine (500g)", "Riz blanc (1.5kg)", "Pâtes (800g)", "Pommes de terre (1.5kg)", "Patate douce x6", "Avocats x6", "Bananes x12", "Flocons d'avoine (1kg)", "Fromage blanc", "Beurre de cacahuète 400g"],
            "prep_tips": ["Mange toutes les 3h maximum", "Post-workout : shaker immédiatement + repas complet 1h après", "Pèse tes aliments pour être précis"],
            "days": [
                make_day(3200,
                    {"name": "Petit-déj XXL", "detail": "100g flocons d'avoine + 400ml lait entier + 4 œufs brouillés + 1 banane + 2 c. beurre cacahuète", "kcal": 920},
                    {"name": "Riz poulet maxi", "detail": "140g riz + 240g poulet + légumes + 2 c. huile olive + sauce soja", "kcal": 880},
                    {"name": "Pâtes bœuf", "detail": "120g pâtes + 170g bœuf haché + sauce tomate + 20g parmesan", "kcal": 820},
                    {"name": "Mass gainer XXL", "detail": "60g flocons + 50g whey + 450ml lait + 1.5 banane + 2 c. beurre cacahuète", "kcal": 820}, "Volume maximal cette semaine."),
                make_day(3100,
                    {"name": "Pancakes protéinés", "detail": "4 œufs + 80g flocons + 300ml lait + 30g whey + sirop + banane", "kcal": 860},
                    {"name": "Bowl saumon riz", "detail": "120g riz + 200g saumon + avocat + épinards + graines", "kcal": 880},
                    {"name": "Poulet patate douce max", "detail": "230g poulet + 280g patate douce + légumes verts + huile olive", "kcal": 750},
                    {"name": "Fromage blanc + noix", "detail": "300g + 50g noix + 2 c. miel", "kcal": 600}, ""),
                make_day(3400,
                    {"name": "Breakfast champion", "detail": "5 œufs + 100g flocons + 400ml lait + banane + 2 c. beurre cacahuète", "kcal": 980},
                    {"name": "Poulet riz ultimate", "detail": "250g poulet + 150g riz + brocolis + courgettes + 3 c. huile olive", "kcal": 950},
                    {"name": "Saumon pâtes max", "detail": "200g saumon + 120g pâtes + épinards + crème légère + parmesan", "kcal": 850},
                    {"name": "Double shaker", "detail": "60g whey + 500ml lait + 2 bananes + 30g flocons", "kcal": 780}, "Journée d'entraînement maximal."),
                make_day(3050,
                    {"name": "Avoine-lait-œufs", "detail": "90g flocons + 3 œufs + banane + 350ml lait entier", "kcal": 820},
                    {"name": "Riz complet bœuf", "detail": "120g riz complet + 180g bœuf + légumes + huile olive", "kcal": 800},
                    {"name": "Dinde + pommes de terre", "detail": "220g dinde + 280g pommes de terre + légumes", "kcal": 680},
                    {"name": "Yaourt grec entier + banane + amandes", "kcal": 500}, ""),
                make_day(3400,
                    {"name": "Gros déj force", "detail": "5 œufs + 100g flocons + 400ml lait + banane + beurre cacahuète", "kcal": 980},
                    {"name": "Poulet riz avocat max", "detail": "250g poulet + 150g riz + 1 avocat + salade + huile olive", "kcal": 920},
                    {"name": "Steak pâtes", "detail": "220g steak + 120g pâtes + tomates + parmesan + herbes", "kcal": 820},
                    {"name": "Mass gainer nuit", "detail": "60g flocons + 50g whey + 500ml lait + banane", "kcal": 820}, "Séance la plus intense de la semaine."),
                make_day(3200,
                    {"name": "Brunch large", "detail": "5 œufs + 3 tranches pain + 1 avocat + saumon fumé 80g + banane", "kcal": 870},
                    {"name": "Repas récupération", "detail": "300g poulet rôti + 250g riz + légumes variés + 2 c. huile olive", "kcal": 900},
                    {"name": "Saumon complet", "detail": "200g saumon + 100g riz complet + brocolis + épinards", "kcal": 680},
                    {"name": "Shaker + noix", "detail": "40g whey + 300ml lait + 40g noix", "kcal": 550}, ""),
                make_day(3000,
                    {"name": "Porridge classique", "detail": "90g flocons + lait + 3 œufs + banane", "kcal": 760},
                    {"name": "Batch S4", "detail": "Prépare les repas de semaine 4", "kcal": 850},
                    {"name": "Poulet légumes complet", "detail": "200g poulet + légumes + riz 100g + huile olive", "kcal": 700},
                    {"name": "Lait + fruits + noix", "kcal": 440}, "Prépare la dernière semaine !"),
            ]
        },
        {
            "week": 4, "theme": "Test de force – Maximiser les gains",
            "intro": "Semaine de test : maintiens le volume calorique élevé pour performer sur les séances max reps.",
            "calories_day": "3 000 – 3 300 kcal",
            "macros": {"proteines": "180g", "glucides": "400g", "lipides": "90g"},
            "shopping_list": ["Poulet (1.2kg)", "Saumon (400g)", "Bœuf (500g)", "Œufs x20", "Lait entier (2L)", "Whey protéine", "Riz blanc (1kg)", "Pâtes (600g)", "Patate douce x5", "Avocats x4", "Bananes x10", "Flocons d'avoine (800g)", "Fromage blanc", "Yaourt grec entier"],
            "prep_tips": ["Ne réduis pas les glucides cette semaine", "Dors minimum 8h – la récupération est cruciale", "Prends des photos avant/après pour voir tes progrès"],
            "days": [
                make_day(3100,
                    {"name": "Petit-déj final", "detail": "90g flocons d'avoine + 350ml lait + 3 œufs + banane + 2 c. beurre cacahuète", "kcal": 850},
                    {"name": "Riz poulet power", "detail": "130g riz + 220g poulet + légumes + huile olive", "kcal": 820},
                    {"name": "Pâtes saumon", "detail": "110g pâtes + 180g saumon + épinards + crème légère", "kcal": 750},
                    {"name": "Mass gainer", "detail": "40g whey + 400ml lait + banane + flocons", "kcal": 620}, "Semaine finale – reste discipliné !"),
                make_day(3000,
                    {"name": "Pancakes masse", "detail": "3 œufs + 80g flocons + 250ml lait + banane + sirop", "kcal": 780},
                    {"name": "Bowl complet", "detail": "110g riz + 200g saumon + avocat + légumes + graines", "kcal": 830},
                    {"name": "Poulet patate douce", "detail": "210g poulet + 250g patate douce + haricots verts", "kcal": 700},
                    {"name": "Fromage blanc + noix", "detail": "300g + 40g noix + miel", "kcal": 550}, ""),
                make_day(3200,
                    {"name": "Breakfast max effort", "detail": "4 œufs + 90g flocons + 350ml lait + banane + beurre cacahuète", "kcal": 880},
                    {"name": "Poulet riz maxi", "detail": "240g poulet + 140g riz + légumes + 2 c. huile olive", "kcal": 870},
                    {"name": "Bœuf pâtes final", "detail": "180g bœuf + 110g pâtes + sauce tomate + fromage", "kcal": 770},
                    {"name": "Shaker récup", "detail": "50g whey + 400ml lait + banane", "kcal": 580}, "Test max effort aujourd'hui !"),
                make_day(2950,
                    {"name": "Avoine-œufs-banane", "detail": "80g flocons + 3 œufs + banane + 300ml lait", "kcal": 750},
                    {"name": "Riz bœuf légumes", "detail": "110g riz + 170g bœuf + légumes + huile olive", "kcal": 760},
                    {"name": "Saumon complet", "detail": "180g saumon + 90g riz complet + épinards", "kcal": 650},
                    {"name": "Yaourt grec + fruits + amandes", "kcal": 480}, ""),
                make_day(3300,
                    {"name": "Grand petit-déj", "detail": "4 œufs + 100g flocons + 400ml lait + banane + 2 c. beurre cacahuète", "kcal": 920},
                    {"name": "Riz poulet avocat", "detail": "140g riz + 240g poulet + 1 avocat + salade", "kcal": 870},
                    {"name": "Steak patates", "detail": "200g steak + 280g pommes de terre + légumes verts", "kcal": 780},
                    {"name": "Mass gainer final", "detail": "60g flocons + 50g whey + 450ml lait + banane + beurre cacahuète", "kcal": 820}, "TEST FINAL – donne absolument tout !"),
                make_day(3100,
                    {"name": "Brunch célébration", "detail": "4 œufs + pain + beurre cacahuète + banane + jus orange", "kcal": 820},
                    {"name": "Repas victoire", "detail": "Mange ce dont tu as envie – tu l'as mérité !", "kcal": 950},
                    {"name": "Saumon léger", "detail": "160g saumon + légumes + riz 80g", "kcal": 580},
                    {"name": "Shaker + fruits", "detail": "40g whey + 300ml lait + fruits", "kcal": 450}, "4 semaines terminées ! Félicitations !"),
                make_day(3000,
                    {"name": "Porridge habituel", "detail": "80g flocons + lait + œufs + banane", "kcal": 740},
                    {"name": "Repas équilibré", "detail": "Poulet + riz + légumes", "kcal": 800},
                    {"name": "Saumon + légumes", "detail": "160g saumon + légumes + féculents", "kcal": 650},
                    {"name": "Collation habituelle", "kcal": 450}, "Continue – ces habitudes sont maintenant les tiennes !"),
            ]
        }
    ],

    "tonification": [
        {
            "week": 1, "theme": "Équilibre alimentaire",
            "intro": "Semaine 1 : maintenance ou léger déficit (-150 kcal). Priorité absolue : les protéines à chaque repas.",
            "calories_day": "1 800 – 2 000 kcal",
            "macros": {"proteines": "150g", "glucides": "200g", "lipides": "65g"},
            "shopping_list": ["Poulet (700g)", "Saumon (400g)", "Œufs x15", "Yaourt grec 0% x8", "Thon boîte x4", "Riz complet", "Quinoa", "Patate douce x4", "Brocolis", "Épinards", "Poivrons", "Avocats x3", "Fruits rouges", "Pommes x6", "Amandes (150g)", "Huile d'olive", "Herbes fraîches"],
            "prep_tips": ["Prépare 500g de protéines en début de semaine", "Coupe les légumes le dimanche soir", "Prépare 3-4 portions de céréales cuites"],
            "days": [
                make_day(1900,
                    {"name": "Omelette + avocat", "detail": "3 œufs + épinards + ½ avocat + 1 tranche pain de seigle + café", "kcal": 430},
                    {"name": "Bowl poulet quinoa", "detail": "140g poulet + 65g quinoa + légumes grillés + vinaigrette huile d'olive-citron", "kcal": 560},
                    {"name": "Saumon + légumes", "detail": "150g saumon vapeur + brocolis + carottes + 70g riz complet", "kcal": 520},
                    {"name": "1 pomme + 20g amandes", "kcal": 175}, "Protéines à chaque repas – c'est la règle numéro 1."),
                make_day(1850,
                    {"name": "Yaourt grec fruits graines", "detail": "200g yaourt grec 0% + 100g fruits rouges + 2 c. graines chia + 10g amandes effilées", "kcal": 320},
                    {"name": "Salade complète", "detail": "Salade niçoise : thon + 2 œufs durs + haricots verts + tomates + olives + vinaigrette légère", "kcal": 530},
                    {"name": "Poulet épices + légumes", "detail": "150g poulet harissa + courgettes + poivrons rôtis + 80g riz complet", "kcal": 520},
                    {"name": "Fromage blanc 0% + miel", "kcal": 130}, "Jour de repos – mange bien quand même."),
                make_day(1950,
                    {"name": "Toast avocat œufs", "detail": "2 tranches pain complet + ½ avocat + 2 œufs pochés + poivre + sel", "kcal": 420},
                    {"name": "Wrap dinde avocat", "detail": "1 tortilla complète + 140g dinde + ½ avocat + salade + tomate + fromage frais 0%", "kcal": 540},
                    {"name": "Filet de poisson", "detail": "170g cabillaud four + légumes vapeur variés + 80g patate douce", "kcal": 450},
                    {"name": "1 orange + 15g noix", "kcal": 185}, "Séance ce soir – collation 1h30 avant."),
                make_day(1800,
                    {"name": "Smoothie protéiné", "detail": "1 banane + 150ml lait végétal + 1 scoop protéine + 30g flocons d'avoine + 1 c. beurre d'amande", "kcal": 380},
                    {"name": "Poulet riz complet", "detail": "140g poulet grillé + 70g riz complet + haricots verts + épinards + huile d'olive", "kcal": 520},
                    {"name": "Omelette légère", "detail": "3 œufs + champignons + épinards + 1 tranche pain seigle", "kcal": 400},
                    {"name": "200g skyr nature + fruits", "kcal": 200}, "Jour calme – reste actif : 20 min marche."),
                make_day(2000,
                    {"name": "Porridge + œufs", "detail": "50g flocons d'avoine + 200ml lait végétal + 2 œufs durs + ½ banane + cannelle", "kcal": 430},
                    {"name": "Bol crevettes quinoa", "detail": "180g crevettes + 65g quinoa + avocat (¼) + tomates cerises + sauce soja légère", "kcal": 570},
                    {"name": "Saumon avocat", "detail": "160g saumon + ½ avocat + brocolis + riz complet 60g", "kcal": 540},
                    {"name": "1 yaourt grec + amandes", "kcal": 200}, "Vendredi – belle semaine ! Dernière séance."),
                make_day(2000,
                    {"name": "Brunch toning", "detail": "3 œufs brouillés + 2 tranches pain complet + ½ avocat + saumon fumé 40g", "kcal": 480},
                    {"name": "Repas social léger", "detail": "Poulet grillé + salade complète + pain complet – mange équilibré", "kcal": 580},
                    {"name": "Soupe + protéine", "detail": "Soupe légumes-pois chiches maison + 1 yaourt grec 0%", "kcal": 380},
                    {"name": "Fruits frais + 10g noix", "kcal": 180}, "Samedi – 1 repas plaisir raisonnable autorisé."),
                make_day(1850,
                    {"name": "Œufs + légumes sautés", "detail": "3 œufs + épinards + poivrons + champignons sautés + café", "kcal": 360},
                    {"name": "Poulet rôti + légumes", "detail": "160g poulet rôti + ratatouille maison + 70g riz complet", "kcal": 540},
                    {"name": "Soupe + yaourt", "detail": "Soupe courgettes-brocolis + 200g yaourt grec 0%", "kcal": 300},
                    {"name": "1 poignée fruits secs", "kcal": 150}, "Prépare ta semaine 2 !"),
            ]
        },
        {
            "week": 2, "theme": "Activation – Boost protéines",
            "intro": "On augmente les protéines de 10% pour mieux tonifier. Glucides autour des séances uniquement.",
            "calories_day": "1 850 – 2 050 kcal",
            "macros": {"proteines": "165g", "glucides": "190g", "lipides": "62g"},
            "shopping_list": ["Poulet (800g)", "Saumon (400g)", "Crevettes (300g)", "Œufs x18", "Skyr x6", "Yaourt grec 0% x6", "Thon boîte x5", "Quinoa", "Riz complet", "Patate douce x4", "Épinards", "Brocolis", "Asperges", "Avocats x4", "Fruits rouges", "Amandes", "Huile d'olive"],
            "prep_tips": ["Augmente la portion protéine de chaque repas", "Mange tes glucides avant/après la séance", "Réduis les glucides le soir si pas de séance"],
            "days": [
                make_day(1950,
                    {"name": "Omelette protéinée", "detail": "4 œufs + épinards + 20g feta légère + 1 tranche pain seigle + café", "kcal": 440},
                    {"name": "Poulet quinoa boost", "detail": "160g poulet + 70g quinoa + avocat (¼) + légumes grillés + vinaigrette citronnée", "kcal": 580},
                    {"name": "Saumon asperges", "detail": "170g saumon papillote + asperges rôties + 80g patate douce + citron", "kcal": 510},
                    {"name": "Skyr 200g + fruits rouges", "kcal": 220}, "Semaine 2 – plus de protéines, même appétit !"),
                make_day(1880,
                    {"name": "Smoothie toning", "detail": "1 banane + 150g fruits rouges + 160ml lait végétal + 1 scoop protéine + 1 c. beurre d'amande", "kcal": 400},
                    {"name": "Salade complète boost", "detail": "2 boîtes thon + 3 œufs durs + haricots verts + tomates + olives + 80g pois chiches", "kcal": 580},
                    {"name": "Dinde légumes vapeur", "detail": "170g dinde vapeur + brocolis + haricots verts + carottes + bouillon", "kcal": 420},
                    {"name": "Fromage blanc 0% + miel", "kcal": 140}, "Repos actif – marche 30 min."),
                make_day(2000,
                    {"name": "Porridge avoine-banane", "detail": "55g flocons + 200ml lait écrémé + ½ banane + 2 œufs durs côté + cannelle", "kcal": 440},
                    {"name": "Bowl crevettes", "detail": "200g crevettes sautées ail-citron + 70g quinoa + concombre + tomates cerises + avocat (¼)", "kcal": 570},
                    {"name": "Poulet rôti légumes", "detail": "170g poulet + courgettes + poivrons + 70g riz complet + herbes", "kcal": 560},
                    {"name": "1 yaourt grec + 20g amandes", "kcal": 220}, "Séance circuit training – mange bien !"),
                make_day(1840,
                    {"name": "Toast protéiné", "detail": "2 tranches pain complet + 2 œufs pochés + ½ avocat + sel poivre + café", "kcal": 400},
                    {"name": "Wrap poulet-avocat", "detail": "1 tortilla complète + 150g poulet + ½ avocat + salade + tomate", "kcal": 520},
                    {"name": "Soupe lentilles + saumon", "detail": "Soupe lentilles corail + légumes (250ml) + 130g saumon grillé", "kcal": 500},
                    {"name": "1 pomme + 15g noix", "kcal": 175}, "Jour calme – hydratation maximale."),
                make_day(2050,
                    {"name": "Œufs-légumes sautés", "detail": "3 œufs + champignons + épinards + poivrons + 1 tranche pain seigle + café", "kcal": 430},
                    {"name": "Bol poulet patate douce", "detail": "170g poulet + 120g patate douce rôtie + épinards + avocat (¼) + sauce tahini légère", "kcal": 590},
                    {"name": "Cabillaud complet", "detail": "180g cabillaud four + légumes méditerranéens + 80g riz complet + huile olive", "kcal": 520},
                    {"name": "Skyr + miel + noix", "kcal": 220}, "Dernière séance de semaine 2 – donne tout !"),
                make_day(2050,
                    {"name": "Brunch équilibré", "detail": "3 œufs brouillés + 2 tranches pain + ½ avocat + tomates + thé/café", "kcal": 460},
                    {"name": "Repas plaisir light", "detail": "Choisis un plat sain mais apprécié – max 650 kcal", "kcal": 650},
                    {"name": "Soupe + protéine légère", "detail": "Soupe légumes + 2 œufs durs + yaourt grec", "kcal": 360},
                    {"name": "Fruits frais + tisane", "kcal": 120}, "Samedi équilibré – 1 repas plaisir autorisé."),
                make_day(1880,
                    {"name": "Porridge classique", "detail": "50g flocons + lait + œufs durs + ½ banane", "kcal": 400},
                    {"name": "Salade complète", "detail": "Poulet froid + légumes + quinoa + vinaigrette", "kcal": 540},
                    {"name": "Légère soupe + yaourt", "detail": "Soupe légumes + 200g yaourt grec", "kcal": 350},
                    {"name": "1 poignée amandes + thé", "kcal": 160}, "Prépare les semaines 3 et 4 – tu avances bien !"),
            ]
        },
        {
            "week": 3, "theme": "Intensification – Corps sculpté",
            "intro": "Semaine 3 : glucides stratégiques autour des séances, protéines au top, graisses saines à chaque repas.",
            "calories_day": "1 850 – 2 050 kcal",
            "macros": {"proteines": "170g", "glucides": "185g", "lipides": "63g"},
            "shopping_list": ["Poulet (800g)", "Saumon (500g)", "Crevettes (300g)", "Œufs x18", "Skyr x8", "Thon boîte x4", "Quinoa", "Riz complet", "Patate douce x4", "Épinards", "Asperges", "Brocolis", "Avocats x4", "Citrons x4", "Fruits rouges", "Amandes", "Noix", "Huile d'olive"],
            "prep_tips": ["Mange les glucides (riz, quinoa, patate douce) uniquement avant/après les séances", "Privilégie légumes + protéines + graisses les jours de repos", "Prépare des bowls de légumes variés"],
            "days": [
                make_day(1950,
                    {"name": "Omelette avocat-épinards", "detail": "4 œufs + épinards + ½ avocat + 1 tranche pain seigle grillé + café", "kcal": 450},
                    {"name": "Bowl saumon quinoa", "detail": "170g saumon + 70g quinoa + concombre + tomates cerises + épinards + vinaigrette sésame", "kcal": 580},
                    {"name": "Poulet asperges", "detail": "170g poulet grillé + asperges rôties + brocolis + 80g patate douce + citron", "kcal": 490},
                    {"name": "Skyr 200g + amandes", "kcal": 235}, "Séance lower body – glucides après l'effort."),
                make_day(1870,
                    {"name": "Yaourt-chia-fruits", "detail": "200g skyr + 2 c. chia + 100g fruits rouges + 15g noix concassées", "kcal": 340},
                    {"name": "Salade protein max", "detail": "140g crevettes + 2 œufs durs + haricots verts + tomates + concombre + avocat + vinaigrette", "kcal": 540},
                    {"name": "Dinde légumes", "detail": "170g dinde + poivrons + courgettes + épinards + 1 c. huile olive", "kcal": 410},
                    {"name": "200g fromage blanc 0% + miel", "kcal": 140}, "Repos – marche 20-30 min."),
                make_day(2000,
                    {"name": "Porridge protéiné", "detail": "50g flocons + 1 scoop protéine + 200ml lait végétal + ½ banane + 1 c. beurre d'amande", "kcal": 440},
                    {"name": "Poulet riz boost", "detail": "170g poulet + 75g riz complet + brocolis + courgettes + herbes + huile olive", "kcal": 570},
                    {"name": "Saumon épinards", "detail": "170g saumon + épinards sautés ail + 80g patate douce + citron", "kcal": 500},
                    {"name": "1 yaourt grec + 20g amandes", "kcal": 220}, "Séance upper body – top !"),
                make_day(1830,
                    {"name": "Toast œufs-avocat", "detail": "2 œufs pochés + ½ avocat + 2 tranches pain de seigle + café", "kcal": 400},
                    {"name": "Wrap toning", "detail": "1 tortilla + 150g poulet épicé + salade + tomate + fromage frais 0% + ½ avocat", "kcal": 530},
                    {"name": "Soupe complète", "detail": "Soupe lentilles-légumes + 120g poulet grillé côté + yaourt grec", "kcal": 490},
                    {"name": "1 pomme + 15g noix", "kcal": 165}, "Jour calme – hydratation."),
                make_day(2050,
                    {"name": "Smoothie bowl toning", "detail": "Base : 1 banane + fruits rouges + lait végétal + 1 scoop protéine. Toppings : noix, graines, 1 c. beurre d'amande", "kcal": 460},
                    {"name": "Bowl crevettes quinoa", "detail": "200g crevettes + 70g quinoa + avocat (¼) + concombre + tomates cerises + sauce sésame", "kcal": 570},
                    {"name": "Poulet tikka light", "detail": "160g poulet mariné yaourt-épices + brocolis + 80g riz complet", "kcal": 500},
                    {"name": "Skyr + miel + graines", "kcal": 210}, "HIIT ce soir – tu vas transpirer !"),
                make_day(2050,
                    {"name": "Brunch sculpt", "detail": "3 œufs + 2 tranches pain + ½ avocat + saumon fumé 40g + café", "kcal": 470},
                    {"name": "Repas équilibré plaisir", "detail": "Repas nourrissant au choix – reste équilibré (protéine + légumes + féculent)", "kcal": 620},
                    {"name": "Dîner léger détox", "detail": "Soupe légumes verts + 1 œuf poché + yaourt grec 0%", "kcal": 310},
                    {"name": "Tisane + fruits frais", "kcal": 110}, "Samedi – dernier repas plaisir avant la semaine finale !"),
                make_day(1870,
                    {"name": "Œufs-légumes dimanche", "detail": "3 œufs + champignons + épinards + poivrons + café", "kcal": 360},
                    {"name": "Salade complète", "detail": "Saumon froid + légumes verts + quinoa + vinaigrette légère", "kcal": 540},
                    {"name": "Soupe + skyr", "detail": "Soupe courgettes-épinards + 200g skyr + 15g noix", "kcal": 370},
                    {"name": "1 poignée amandes + thé vert", "kcal": 165}, "Dimanche récup – semaine 4, la dernière !"),
            ]
        },
        {
            "week": 4, "theme": "Final Toning – Corps défini",
            "intro": "Dernière semaine ! Maintiens tout ce que tu as appris. Résultats visibles – photos avant/après !",
            "calories_day": "1 850 – 2 000 kcal",
            "macros": {"proteines": "175g", "glucides": "180g", "lipides": "62g"},
            "shopping_list": ["Poulet (900g)", "Saumon (500g)", "Crevettes (300g)", "Œufs x18", "Skyr x8", "Yaourt grec 0% x6", "Quinoa", "Riz complet", "Patate douce x4", "Asperges", "Épinards", "Brocolis", "Avocats x5", "Citrons x5", "Fruits rouges", "Amandes", "Graines de chia"],
            "prep_tips": ["Batch cook maximum ce dimanche", "Pèse tes portions pour suivre tes apports", "Prends tes photos avant/après le lundi matin"],
            "days": [
                make_day(1950,
                    {"name": "Petit-déj final toning", "detail": "3 œufs + ½ avocat + 1 tranche pain seigle + café ou thé vert", "kcal": 400},
                    {"name": "Bowl saumon final", "detail": "170g saumon + 70g quinoa + avocat (¼) + épinards + tomates cerises + vinaigrette citron", "kcal": 580},
                    {"name": "Poulet asperges final", "detail": "170g poulet + asperges + brocolis + 80g patate douce", "kcal": 480},
                    {"name": "Skyr 200g + fruits rouges", "kcal": 225}, "Semaine finale – corps sculpté en approche !"),
                make_day(1880,
                    {"name": "Smoothie toning", "detail": "1 banane + fruits rouges + 150ml lait végétal + 1 scoop protéine + 1 c. beurre d'amande", "kcal": 400},
                    {"name": "Salade crevettes-avocat", "detail": "200g crevettes + avocat + salade verte + tomates + concombre + vinaigrette légère", "kcal": 520},
                    {"name": "Dinde-légumes vapeur", "detail": "170g dinde + haricots verts + brocolis + carottes + 1 c. huile olive", "kcal": 410},
                    {"name": "200g fromage blanc 0% + miel", "kcal": 145}, "2 jours avant la fin – garde le cap !"),
                make_day(2000,
                    {"name": "Porridge toning", "detail": "50g flocons + 1 scoop protéine + lait végétal + ½ banane + 1 c. beurre d'amande", "kcal": 440},
                    {"name": "Poulet riz légumes", "detail": "170g poulet + 75g riz complet + brocolis + courgettes + huile olive", "kcal": 570},
                    {"name": "Saumon complet", "detail": "170g saumon + épinards + asperges + citron + 80g patate douce", "kcal": 510},
                    {"name": "1 yaourt grec + 20g amandes", "kcal": 225}, "Avant-dernière séance – donne tout !"),
                make_day(1820,
                    {"name": "Toast avocat-saumon", "detail": "2 tranches pain seigle + ½ avocat + 40g saumon fumé + câpres + citron", "kcal": 390},
                    {"name": "Bowl complet toning", "detail": "150g poulet + 70g quinoa + avocat (¼) + légumes grillés + vinaigrette tahini", "kcal": 550},
                    {"name": "Soupe protéinée", "detail": "Soupe lentilles + légumes + 1 œuf poché + yaourt grec", "kcal": 450},
                    {"name": "1 pomme + 15g noix", "kcal": 165}, "Calme avant la dernière séance."),
                make_day(2000,
                    {"name": "Breakfast champion final", "detail": "3 œufs + épinards + ½ avocat + 2 tranches pain complet + café", "kcal": 440},
                    {"name": "Bowl puissance finale", "detail": "170g crevettes + 70g quinoa + avocat + tomates cerises + épinards + sauce citron-sésame", "kcal": 570},
                    {"name": "Saumon asperges final", "detail": "170g saumon + asperges + brocolis + patate douce 90g + herbes", "kcal": 500},
                    {"name": "Skyr + graines chia + miel", "kcal": 215}, "DERNIÈRE SÉANCE – donne absolument tout !"),
                make_day(2000,
                    {"name": "Brunch toning victoire", "detail": "3 œufs brouillés + 2 tranches pain + ½ avocat + fruits frais", "kcal": 470},
                    {"name": "Repas plaisir mérité", "detail": "Tu as terminé ! Mange ce que tu aimes – tu le mérites !", "kcal": 650},
                    {"name": "Dîner léger", "detail": "Soupe légumes + yaourt grec", "kcal": 280},
                    {"name": "Tisane relaxante", "kcal": 0}, "4 SEMAINES TERMINÉES – FÉLICITATIONS ! Prends tes photos bilan."),
                make_day(1870,
                    {"name": "Petit-déj habituel", "detail": "Œufs ou porridge selon envie", "kcal": 400},
                    {"name": "Repas équilibré", "detail": "Poulet/poisson + légumes + féculents", "kcal": 540},
                    {"name": "Dîner léger", "detail": "Soupe + protéine légère + yaourt", "kcal": 350},
                    {"name": "Collation légère habituelle", "kcal": 170}, "Ces nouvelles habitudes sont maintenant les tiennes – continue !"),
            ]
        }
    ]
}

# ─── NUTRITION PLANS ──────────────────────────────────────────────────────────

NUTRITION = {
    "perte_poids": {
        "name": "Nutrition – Perte de poids",
        "calories_target": "déficit de 300-500 kcal/jour",
        "macro_split": {"proteines": "30%", "glucides": "40%", "lipides": "30%"},
        "principles": [
            "Boire minimum 2,5L d'eau par jour",
            "Privilégier les protéines à chaque repas (viande maigre, œufs, légumineuses)",
            "Éviter les sucres rapides et les aliments ultra-transformés",
            "Manger lentement et s'arrêter avant d'avoir trop faim",
            "Pas de privation extrême : 1 repas plaisir par semaine autorisé",
        ],
        "meal_plan": {
            "Petit-déjeuner": [
                "Flocons d'avoine (60g) + lait végétal + 1 banane + 1 cuillère de beurre de cacahuète",
                "Omelette 3 œufs + 2 tranches pain complet + café sans sucre",
                "Yaourt grec 0% + granola maison + fruits rouges",
            ],
            "Déjeuner": [
                "Poulet grillé (150g) + riz complet (80g cru) + légumes rôtis",
                "Salade composée : thon, pois chiches, tomates, concombre + vinaigrette légère",
                "Saumon (150g) + quinoa (70g cru) + brocolis vapeur",
            ],
            "Dîner": [
                "Soupe de légumes + 2 œufs durs + 1 tranche pain complet",
                "Blanc de dinde (120g) + patate douce (150g) + salade verte",
                "Lentilles corail (80g cru) + légumes poêlés + yaourt grec",
            ],
            "Collation": [
                "1 pomme + 15g d'amandes",
                "Fromage blanc 0% + 1 cuillère miel",
                "1 banane + 1 poignée de noix de cajou",
            ]
        },
        "foods_to_avoid": ["Sodas et jus de fruits industriels", "Fast-food", "Plats préparés", "Chips et gâteaux industriels", "Alcool (limiter fortement)"],
        "foods_to_favor": ["Légumes verts à volonté", "Protéines maigres", "Fruits entiers", "Céréales complètes", "Graisses saines (avocat, noix, huile d'olive)"]
    },
    "prise_masse": {
        "name": "Nutrition – Prise de masse",
        "calories_target": "surplus de 250-400 kcal/jour",
        "macro_split": {"proteines": "25%", "glucides": "50%", "lipides": "25%"},
        "principles": [
            "Manger toutes les 3-4h pour maintenir l'anabolisme",
            "1,8-2g de protéines par kg de poids corporel",
            "Ne jamais sauter de repas",
            "Préférer les calories nutritives aux calories vides",
            "S'hydrater suffisamment (2-3L d'eau)",
        ],
        "meal_plan": {
            "Petit-déjeuner": [
                "6 blancs d'œufs + 2 jaunes + flocons d'avoine (80g) + lait entier + banane",
                "Pancakes protéinés (whey + avoine + œufs) + sirop d'érable + fruits",
                "Pain complet (3 tranches) + beurre de cacahuète + 3 œufs brouillés",
            ],
            "Déjeuner": [
                "Riz blanc (120g cru) + poulet (200g) + légumes + huile d'olive",
                "Pâtes complètes (100g cru) + viande hachée 5% (150g) + sauce tomate maison",
                "Pommes de terre (300g) + steak (200g) + haricots verts",
            ],
            "Dîner": [
                "Saumon (180g) + patate douce (200g) + épinards",
                "Porc maigre (170g) + riz (100g cru) + brocolis",
                "Thon (2 boîtes) + pâtes (90g cru) + tomates + fromage",
            ],
            "Collation": [
                "Shaker : 30g whey + lait + 1 banane + 30g flocons d'avoine",
                "200g fromage blanc + 30g noix + 1 fruit",
                "4 galettes de riz + 60g beurre de cacahuète + yaourt grec",
            ]
        },
        "foods_to_avoid": ["Alcool", "Sucres raffinés en excès", "Fast-food (mauvaises graisses)"],
        "foods_to_favor": ["Riz, pâtes, pommes de terre", "Viandes maigres + poissons", "Œufs entiers", "Légumineuses", "Noix et graines", "Produits laitiers"]
    },
    "tonification": {
        "name": "Nutrition – Tonification",
        "calories_target": "maintenance ou léger déficit (-200 kcal)",
        "macro_split": {"proteines": "35%", "glucides": "35%", "lipides": "30%"},
        "principles": [
            "Protéines élevées pour préserver le muscle",
            "Glucides autour des séances d'entraînement",
            "Graisses saines à chaque repas",
            "Éviter les fringales avec des collations équilibrées",
        ],
        "meal_plan": {
            "Petit-déjeuner": [
                "Omelette 3 œufs + avocat + pain de seigle",
                "Yaourt grec + fruits rouges + graines de chia + amandes",
                "Smoothie : lait végétal + protéine + épinards + banane + beurre d'amande",
            ],
            "Déjeuner": [
                "Poulet (150g) + quinoa (60g cru) + légumes grillés + huile d'olive",
                "Salade niçoise : thon + œuf + haricots verts + tomates + olives",
                "Wrap complet : dinde + légumes + fromage frais + avocat",
            ],
            "Dîner": [
                "Poisson blanc (150g) + légumes vapeur + riz complet (50g cru)",
                "Omelette champignons + épinards + 1 tranche pain complet",
                "Soupe protéinée : lentilles + légumes + œuf poché",
            ],
            "Collation": [
                "1 pomme + 20g amandes",
                "Fromage blanc 0% + 1 cuillère miel + noix",
                "Bâtonnets de légumes + houmous maison",
            ]
        },
        "foods_to_avoid": ["Sucres ajoutés", "Alcool", "Graisses trans", "Snacks industriels"],
        "foods_to_favor": ["Protéines à chaque repas", "Légumes verts", "Graisses saines", "Glucides complexes"]
    }
}


def get_program(goal, equipment, level):
    """Return the appropriate workout and nutrition plan."""
    if goal == "perte_poids":
        workout_key = "perte_poids_maison"
        nutrition_key = "perte_poids"
    elif goal == "prise_masse":
        workout_key = "prise_masse_maison"
        nutrition_key = "prise_masse"
    else:
        workout_key = "tonification_maison"
        nutrition_key = "tonification"

    return {
        "workout": WORKOUTS[workout_key],
        "nutrition": NUTRITION[nutrition_key],
        "nutrition_weeks": NUTRITION_WEEKS[nutrition_key]
    }
