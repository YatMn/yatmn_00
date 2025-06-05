import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user_and_list():
    response = client.post('/users', json={'id': 1, 'name': 'Alice', 'email': 'a@example.com'})
    assert response.status_code == 200
    user = response.json()
    assert user['name'] == 'Alice'

    response = client.get('/therapists')
    assert response.status_code == 200
    therapists = response.json()
    assert len(therapists) >= 2

    response = client.post('/appointments', json={'id': 1, 'user_id': 1, 'therapist_id': 1, 'time': '2024-01-01T10:00'})
    assert response.status_code == 200
    appt = response.json()
    assert appt['user_id'] == 1

    response = client.get('/appointments')
    assert response.status_code == 200
    appts = response.json()
    assert len(appts) == 1
