from pydantic import BaseModel,Field,field_validator
class UserInput(BaseModel):
    user_id:str=Field(min_length=1,max_length=100); name:str=Field(min_length=1,max_length=120)
    age:int=Field(ge=13,le=100); weight:float=Field(gt=20,lt=400); goal:str; intensity:str
    @field_validator("goal")
    @classmethod
    def goal_ok(cls,v):
        v=v.strip().lower()
        if v not in {"weight loss","muscle gain","general wellness","flexibility"}: raise ValueError("Invalid goal")
        return v
    @field_validator("intensity")
    @classmethod
    def intensity_ok(cls,v):
        v=v.strip().lower()
        if v not in {"low","medium","high"}: raise ValueError("Invalid intensity")
        return v
