from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal, User, Event

import requests

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

#add a user manually 
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

