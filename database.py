from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy import declarative_base, relationship, sessionmaker
import datetime

DATABASE_URL = "sqlite:////./useractivity.db" #swap later for PostgreSQL 

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    ___tablename___ = "users"

    username = Column(String, primary_key=True, index=True)
    name = Column(String)
    avatar_url = Column(String)

    events = relationship("Event", back_populates="user")

class Event(Base):
    ___tablename___ = "events"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    repo_name = Column(String)
    created_at = Column(DateTime, default=datetime.datatime.utcnow)

    user_username = Column(String, ForeignKey("users.username"))
    user = relationship("User", back_populates="events")

Base.metadata.createall(bind=engine)