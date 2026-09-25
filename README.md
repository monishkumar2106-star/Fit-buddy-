# FitBuddy MVP
FastAPI + Jinja2 + SQLite + optional Gemini integration.
## Windows
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
Open http://127.0.0.1:8000 and /docs.
If no Gemini key is supplied, the MVP uses a local fallback so it remains runnable.
