from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
BASE_DIR=Path(__file__).resolve().parent.parent
DATA_DIR=BASE_DIR/"data"; DATA_DIR.mkdir(exist_ok=True)
engine=create_engine(f"sqlite:///{DATA_DIR/'fitbuddy.db'}",connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()
def init_db():
    from . import models
    Base.metadata.create_all(bind=engine)
def get_db():
    init_db()
    db=SessionLocal()
    try: yield db
    finally: db.close()
