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
        "nutrition": NUTRITION[nutrition_key]
    }
