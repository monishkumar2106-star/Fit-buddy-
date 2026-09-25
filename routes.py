from pathlib import Path
from fastapi import APIRouter,Depends,Form,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import UserInput
from .models import User,Plan
from .services import save_user,save_plan,latest_plan,update_plan
from .ai.workout_generator import generate_workout_gemini
from .ai.nutrition_generator import generate_nutrition_tip_with_flash
from .ai.plan_updater import update_workout_plan
templates=Jinja2Templates(directory=str(Path(__file__).resolve().parent.parent/"templates"))
router=APIRouter()
@router.get("/",response_class=HTMLResponse)
def home(request:Request): return templates.TemplateResponse(request=request, name="index.html", context={})
@router.post("/generate-workout",response_class=HTMLResponse)
def generate(request:Request,user_id:str=Form(...),name:str=Form(...),age:int=Form(...),weight:float=Form(...),goal:str=Form(...),intensity:str=Form(...),db:Session=Depends(get_db)):
    d=UserInput(user_id=user_id,name=name,age=age,weight=weight,goal=goal,intensity=intensity)
    plan=generate_workout_gemini(d.name,d.age,d.weight,d.goal,d.intensity); tip=generate_nutrition_tip_with_flash(d.goal)
    save_user(db,d); save_plan(db,d.user_id,plan,tip)
    return templates.TemplateResponse(request=request, name="result.html", context={"request":request,"user":d,"workout_plan":plan,"nutrition_tip":tip,"updated_plan":None,"message":None})
@router.post("/submit-feedback",response_class=HTMLResponse)
def feedback(request:Request,user_id:str=Form(...),feedback:str=Form(...),db:Session=Depends(get_db)):
    p=latest_plan(db,user_id);u=db.query(User).filter(User.user_id==user_id).first()
    if not p or not u:return templates.TemplateResponse(request=request, name="error.html", context={"request":request,"message":"User or plan not found."}, status_code=404)
    revised=update_workout_plan(p.original_plan,feedback);update_plan(db,p,revised,feedback)
    d=UserInput(user_id=u.user_id,name=u.name,age=u.age,weight=u.weight,goal=u.goal,intensity=u.intensity)
    return templates.TemplateResponse(request=request, name="result.html", context={"request":request,"user":d,"workout_plan":p.original_plan,"nutrition_tip":p.nutrition_tip,"updated_plan":revised,"message":"Plan updated successfully."})
@router.get("/view-all-users",response_class=HTMLResponse)
def users(request:Request,db:Session=Depends(get_db)):
    us=db.query(User).order_by(User.id.desc()).all()
    plans={u.user_id:latest_plan(db,u.user_id) for u in us}
    return templates.TemplateResponse(request=request, name="all_users.html", context={"request":request,"users":us,"plans":plans})
