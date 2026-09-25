from .fallback import workout as fallback_workout,nutrition as fallback_nutrition
from ..config import GEMINI_API_KEY,GEMINI_MODEL
_client=None
def text(prompt):
    global _client
    if not GEMINI_API_KEY:return None
    try:
        from google import genai
        if _client is None:_client=genai.Client(api_key=GEMINI_API_KEY)
        r=_client.models.generate_content(model=GEMINI_MODEL,contents=prompt)
        return getattr(r,"text",None)
    except Exception:return None
def generate_workout(name,age,weight,goal,intensity):
    p=f"Create a safe practical 7-day workout plan for {name}, age {age}, weight {weight} kg, goal {goal}, intensity {intensity}. Include warm-up, exercises with sets/reps or duration, rest and cooldown."
    return text(p) or fallback_workout(name,goal,intensity)
def generate_nutrition(goal):
    return text(f"Give one concise practical nutrition or recovery tip for fitness goal {goal}. Avoid extreme diets.") or fallback_nutrition(goal)
def revise(original,feedback):
    return text(f"Revise this fitness plan according to feedback. Original:\n{original}\nFeedback:\n{feedback}\nReturn a complete practical safe plan with a rest day.") or (original+"\n\nUPDATED FEEDBACK:\n"+feedback)
