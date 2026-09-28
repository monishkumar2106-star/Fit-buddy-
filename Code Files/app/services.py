from .models import User,Plan
def save_user(db,data):
    u=db.query(User).filter(User.user_id==data.user_id).first()
    if u:
        u.name,u.age,u.weight,u.goal,u.intensity=data.name,data.age,data.weight,data.goal,data.intensity
    else: u=User(**data.model_dump()); db.add(u)
    db.commit(); db.refresh(u); return u
def save_plan(db,user_id,original,tip):
    p=Plan(user_id=user_id,original_plan=original,nutrition_tip=tip); db.add(p); db.commit(); db.refresh(p); return p
def latest_plan(db,user_id): return db.query(Plan).filter(Plan.user_id==user_id).order_by(Plan.id.desc()).first()
def update_plan(db,p,revised,feedback):
    p.updated_plan=revised;p.feedback=feedback;db.commit();db.refresh(p);return p
