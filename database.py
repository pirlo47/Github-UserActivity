from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

"""
This module defines the SQLAlchemy ORM models and database setup for tracking GitHub user activity.

Classes:
    User: Represents a GitHub user with username, name, and avatar URL.
    Event: Represents an activity event associated with a user, including event type, repository name, and timestamp.

Database:
    Uses SQLite for local storage (can be swapped for PostgreSQL).
    Establishes engine, session, and base declarative class.
"""

"""
ORM model for a GitHub user.

Attributes:
    username (str): Primary key, GitHub username.
    name (str): Display name of the user.
    avatar_url (str): URL to the user's avatar image.
    events (List[Event]): Relationship to associated Event objects.
"""

"""
ORM model for a GitHub activity event.

Attributes:
    id (int): Primary key, unique event identifier.
    type (str): Type of the event (e.g., push, pull request).
    repo_name (str): Name of the repository where the event occurred.
    created_at (datetime): Timestamp of when the event was created.
    user_username (str): Foreign key referencing the associated user's username.
    user (User): Relationship to the associated User object.
"""

DATABASE_URL = "sqlite:////./useractivity.db" #swap later for PostgreSQL 

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    name = Column(String)
    avatar_url = Column(String)

    events = relationship("Event", back_populates="user")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    repo_name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user_username = Column(String, ForeignKey("users.username"))
    user = relationship("User", back_populates="events")

Base.metadata.create_all(bind=engine)