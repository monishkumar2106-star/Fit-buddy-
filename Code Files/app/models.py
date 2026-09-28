from sqlalchemy import Column,Integer,Float,String,Text,DateTime
from sqlalchemy.sql import func
from .database import Base
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    user_id=Column(String(100),unique=True,index=True,nullable=False)
    name=Column(String(120),nullable=False); age=Column(Integer,nullable=False)
    weight=Column(Float,nullable=False); goal=Column(String(80),nullable=False)
    intensity=Column(String(20),nullable=False); created_at=Column(DateTime(timezone=True),server_default=func.now())
class Plan(Base):
    __tablename__="plans"
    id=Column(Integer,primary_key=True); user_id=Column(String(100),index=True,nullable=False)
    original_plan=Column(Text,nullable=False); updated_plan=Column(Text)
    nutrition_tip=Column(Text,nullable=False); feedback=Column(Text)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
