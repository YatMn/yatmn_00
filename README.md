# Mental Health Counseling App

This repository contains a minimal FastAPI backend demonstrating a prototype mental health counseling service.

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
uvicorn app.main:app --reload
```

This will start a server at `http://127.0.0.1:8000` with API documentation available at `/docs`.

## API Endpoints
- `POST /users` – create a new user.
- `GET /therapists` – list available therapists.
- `POST /appointments` – create an appointment.
- `GET /appointments` – list appointments.
