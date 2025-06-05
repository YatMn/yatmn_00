from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Mental Health Counseling API")

class User(BaseModel):
    id: int
    name: str
    email: str

class Therapist(BaseModel):
    id: int
    name: str
    specialty: str

class Appointment(BaseModel):
    id: int
    user_id: int
    therapist_id: int
    time: str

users: Dict[int, User] = {}
therapists: Dict[int, Therapist] = {
    1: Therapist(id=1, name="Dr. Zhang", specialty="Depression"),
    2: Therapist(id=2, name="Dr. Li", specialty="Anxiety"),
}
appointments: Dict[int, Appointment] = {}

@app.post("/users", response_model=User)
def create_user(user: User):
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.id] = user
    return user

@app.get("/therapists", response_model=List[Therapist])
def list_therapists():
    return list(therapists.values())

@app.post("/appointments", response_model=Appointment)
def create_appointment(appt: Appointment):
    if appt.id in appointments:
        raise HTTPException(status_code=400, detail="Appointment already exists")
    if appt.user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    if appt.therapist_id not in therapists:
        raise HTTPException(status_code=404, detail="Therapist not found")
    appointments[appt.id] = appt
    return appt

@app.get("/appointments", response_model=List[Appointment])
def list_appointments():
    return list(appointments.values())

