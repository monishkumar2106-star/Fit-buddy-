from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_home(): assert client.get("/").status_code==200
def test_docs(): assert client.get("/docs").status_code==200


def test_generate_workout_without_gemini():
    response = client.post("/generate-workout", data={
        "user_id": "test-user",
        "name": "Alex",
        "age": "18",
        "weight": "70",
        "goal": "general wellness",
        "intensity": "medium",
    })
    assert response.status_code == 200
    assert "Alex" in response.text
    assert "7-Day Workout Plan" in response.text


def test_feedback_updates_plan():
    client.post("/generate-workout", data={
        "user_id": "feedback-user",
        "name": "Sam",
        "age": "20",
        "weight": "68",
        "goal": "flexibility",
        "intensity": "low",
    })
    response = client.post("/submit-feedback", data={
        "user_id": "feedback-user",
        "feedback": "Add a little more mobility work.",
    })
    assert response.status_code == 200
    assert "Updated Plan" in response.text


def test_feedback_unknown_user_returns_404():
    response = client.post("/submit-feedback", data={
        "user_id": "missing-user",
        "feedback": "Please revise",
    })
    assert response.status_code == 404
