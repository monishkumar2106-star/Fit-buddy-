def workout(name,goal,intensity):
    return f'''FITBUDDY 7-DAY PLAN FOR {name.upper()}
Goal: {goal.title()} | Intensity: {intensity.title()}

Day 1 – Full Body: Warm-up 8 min. Squats 3x10, Push-ups 3x8-12, Rows 3x10, Plank 3x30 sec. Cooldown 5 min.
Day 2 – Cardio + Core: 25 min brisk walk/cycle. Dead Bug 3x10, Bird Dog 3x10. Stretch 5 min.
Day 3 – Lower Body: Squats 3x10, Lunges 3x8/leg, Glute Bridge 3x12, Calf Raise 3x15.
Day 4 – Active Recovery: 20-30 min easy walk plus gentle mobility.
Day 5 – Upper Body: Incline Push-ups 3x10, Rows 3x10, Shoulder Press 3x10, Curls 2x12.
Day 6 – Full Body + Cardio: Squats 3x12, Push-ups 3x10, Rows 3x10, 15-20 min easy cardio.
Day 7 – Rest / Recovery: Easy movement if comfortable, hydration, sleep and recovery.

Adjust exercise difficulty to your ability and stop for pain, dizziness, or unusual symptoms.'''
def nutrition(goal):
    return {"weight loss":"Build meals around vegetables, a protein source, high-fibre foods and water; keep portions consistent.",
    "muscle gain":"Include a protein source in each main meal and eat enough overall to support training.",
    "general wellness":"Aim for balanced meals with vegetables or fruit, protein, high-fibre carbohydrates and adequate water.",
    "flexibility":"Support training with balanced meals, adequate protein, fruit and vegetables, and good hydration."}.get(goal,"Choose balanced meals and stay hydrated.")
