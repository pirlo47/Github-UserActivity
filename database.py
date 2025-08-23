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