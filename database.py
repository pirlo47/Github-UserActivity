from dotenv import load_dotenv 
from pymongo import MongoClient, ASCENDING
import os 

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client["github-activity-dev"]

users = db["users"]
events = db["events"]

#set _id = github event id, so dedupe is automatic and needs no index.
events.create_index([("username", ASCENDING)])
events.create_index([("created_at", ASCENDING)])

