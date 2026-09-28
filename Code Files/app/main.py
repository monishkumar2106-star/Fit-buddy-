from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import init_db
from .routes import router
BASE_DIR=Path(__file__).resolve().parent.parent
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app=FastAPI(title="FitBuddy – AI Fitness Plan Generator",version="1.0.0", lifespan=lifespan)
app.mount("/static",StaticFiles(directory=str(BASE_DIR/"static")),name="static")
app.include_router(router)
