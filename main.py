__version__ = "1.0.0"

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal, User, Event
from pydantic import BaseModel
import requests
"""
main.py
FastAPI application for tracking GitHub user activity.
Endpoints:
- GET /: Root endpoint to check API status.
- POST /user/: Add a GitHub user to the database by username.
- GET /users/: List all users in the database.
- POST /users/{username}/events: Fetch and save GitHub events for a user.
- GET /users/{username}/events: Retrieve saved events for a user.
Dependencies:
- get_db: Provides a SQLAlchemy database session.
Models:
- UserCreate: Pydantic model for user creation.
Database:
- Uses SQLAlchemy ORM models: User, Event.
- Session management via SessionLocal.
External APIs:
- Fetches user and event data from GitHub public API.
Error Handling:
- Returns HTTP 404 if user or events are not found on GitHub or in the database.
"""

app = FastAPI()


#Dependency for DB session 
def get_db():
    db = SessionLocal()
    try: 
        yield db 
    finally:
        db.close()
    
#Root endpoint 
@app.get("/")
def read_root():
    return {"message":"Github User Activity API is running!"}

class UserCreate(BaseModel):
    username: str 


#add a user manually
@app.post("/user/") 
def create_user(username: str, db: Session = Depends(get_db)):
    #Fetch data from the Github API 
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=404, detail="User not found")
    data = r.json()

    user = User(username=data["login"], name=data.get("name"), avatar_url=data.get("avatar_url"))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user 

#Get all users 
@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

#Fetch and save events for a user 
@app.post("/users/{username}/events")
def fetch_events(username: str, db: Session = Depends(get_db)):
    url = f"https://api.github.com/users/{username}/events"
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Events for user {username} not found")
    data = r.json()

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User not in database")
    
    for e in data:
        event = Event(
            type=e["type"],
            repo_name=e["repo"]["name"],
        )
        event.user = user 
        db.add(event)
    db.commit()
    return {"message": f"Events for {username} saved."}

#Get events for a user 
@app.get("/users/{username}/events")
def get_events(username: str, db: Session = Depends(get_db)):
    return db.query(Event).filter(Event.user_username == username).all()

