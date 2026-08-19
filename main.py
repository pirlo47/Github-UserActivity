from fastapi import FastAPI, HTTPException
from pymongo import UpdateOne
from datetime import datetime, timezone
import requests
import os
from database import users, events

app = FastAPI()


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def github_headers() -> dict:
    """
       Auth + recommended headers for te github rest API.
    """
    headers = {
        "Accept": "application/vnd.github+json", 
        "X-Github-Api-Version": "2022-11-28", 
    }
    if GITHUB_TOKEN: 
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers

    
def parse_github_time(value: str ) -> datetime:
    """
    helper func to convert github timestamp into native UTC datetime
    """

    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return dt.astimezone(timezone.utc).replace(tzinfo=None)

def extract_event_fields(e: dict) -> dict:
    """Pull metric-relevant fields out of a GitHub event's payload.
    Unknown event types simply return Nones — nothing breaks."""

    payload = e.get("payload") or {}
    etype = e.get("type")

    fields = {
        "action": payload.get("action"),
        "commit_count": None,
        "pr_merged": None,
        "pr_created_at": None,
        "pr_merged_at": None,
    }

    if etype == "PushEvent":
        # payload.size = number of commits in this push
        fields["commit_count"] = payload.get("size", len(payload.get("commits", [])))

    elif etype == "PullRequestEvent":
        pr = payload.get("pull_request") or {}
        fields["pr_merged"] = pr.get("merged")
        if pr.get("created_at"):
            fields["pr_created_at"] = parse_github_time(pr["created_at"])
        if pr.get("merged_at"):
            fields["pr_merged_at"] = parse_github_time(pr["merged_at"])

    return fields

#Root endpoint 
@app.get("/")
def read_root():
    return {"message": "Github User Activity API is running!"}

@app.post("/user/")
def create_user(username: str):
    r = requests.get(f"https://api.github.com/users/{username}", headers=github_headers())
    if r.status_code != 200:
        raise HTTPException(status_code=404, detail="User not found")
    data = r.json()
    doc = {"_id": data["login"], "name": data.get("name"), "avatar_url": data.get("avatar_url")}
    users.replace_one({"_id": data["login"]}, doc, upsert=True)  # idempotent add
    return doc

@app.get("/users/")
def list_users():
    return list(users.find())

@app.post("/users/{username}/events")
def fetch_events(username: str):
    r = requests.get(f"https://api.github.com/users/{username}/events", headers=github_headers())
    if r.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Events for user {username} not found")
    data = r.json()

    if not users.find_one({"_id": username}):
        raise HTTPException(status_code=404, detail="User not in database")

    ops = []
    for e in data:
        fields = extract_event_fields(e)
        doc = {
            "_id": e["id"],                         # github event id = dedupe key
            "username": username,
            "type": e["type"],
            "repo_name": e["repo"]["name"],
            "created_at": parse_github_time(e["created_at"]),
            **fields,                               # action, commit_count, pr_merged, ...
            "payload": e.get("payload"),            # full raw document retained
        }
        # $setOnInsert writes only when _id is new — re-fetches are no-ops
        ops.append(UpdateOne({"_id": e["id"]}, {"$setOnInsert": doc}, upsert=True))

    new_count = 0
    if ops:
        result = events.bulk_write(ops, ordered=False)
        new_count = result.upserted_count

    return {"message": f"Saved {new_count} new events for {username}; {len(data) - new_count} already stored."}

@app.get("/users/{username}/events")
def get_events(username: str):
    return list(events.find({"username": username}).sort("created_at", -1))