# 🚀 GitHub User Activity Tracker

A FastAPI + MongoDB application that tracks GitHub users and their activity. It fetches
user details and recent events from the GitHub REST API, stores them in MongoDB, and
exposes them through a REST API.

The goal is to grow this into a **throughput / effectiveness tracker** — a tool that shows
how quickly and effectively someone works on GitHub, visualised as graphs, tables, and
charts (see [Roadmap](#-roadmap)).

## ✨ Features
- Fetch and store GitHub user details (username, name, avatar URL)
- Fetch and store user activity events with their **real GitHub timestamps**
- **Idempotent ingestion** — events are de-duplicated on the GitHub event id, so re-fetching
  never creates duplicates
- **Rich payload capture** — commit counts, pull-request actions and merge data are extracted
  for metrics, and the full raw event payload is retained
- **GitHub token support** — raises the API rate limit from 60 to 5,000 requests/hour
- Auto-generated API docs (Swagger UI / ReDoc)

## 🧱 Tech Stack
- **FastAPI** — web framework / REST API
- **MongoDB** — document database (MongoDB Atlas free tier, or local via Docker)
- **PyMongo** — MongoDB driver
- **GitHub REST API** — data source

## 📂 Project Structure
```
.
├── main.py             # FastAPI app, endpoints, and GitHub ingestion logic
├── database.py         # MongoDB client + collection handles (users, events)
├── docker-compose.yml  # Local MongoDB container (optional alternative to Atlas)
├── .env                # Environment variables (MONGO_URL, GITHUB_TOKEN)
├── requirements.txt    # Python dependencies
└── README.md
```

## 🔧 Prerequisites
- Python 3.10+
- A MongoDB database — either a free **MongoDB Atlas** cluster or a local **Docker** container
- pip
- A **GitHub Personal Access Token** (recommended — avoids the 60 req/hour unauthenticated limit)

## ⚙️ Environment Configuration
Create a `.env` file in the project root:

```bash
# .env

# MongoDB Atlas (recommended — free M0 tier):
MONGO_URL=mongodb+srv://<user>:<url_encoded_password>@<cluster>.mongodb.net/?retryWrites=true&w=majority

# ...or local MongoDB via Docker (this is also the default if MONGO_URL is unset):
# MONGO_URL=mongodb://localhost:27017

# GitHub token (no scopes needed for public data):
GITHUB_TOKEN=github_pat_xxxxxxxxxxxxxxxxx
```

Notes:
- If `MONGO_URL` is omitted, the app falls back to `mongodb://localhost:27017`.
- `mongodb+srv://` (Atlas) URIs require `dnspython`, installed via `pymongo[srv]`.
- URL-encode special characters in the password (`@` → `%40`, etc.).

## 📦 Installation
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🗄️ Running MongoDB

### Option A — MongoDB Atlas (recommended)
Create a free M0 cluster, add a database user and your IP to the Network Access allowlist,
then put the connection string in `.env` as `MONGO_URL`. Nothing to run locally.

### Option B — Local MongoDB via Docker
```bash
docker compose up -d
docker ps          # verify the github_activity_mongo container is running
```
Uses `mongodb://localhost:27017` (leave `MONGO_URL` unset or set it to that value).

## 🧩 Running the API
```bash
uvicorn main:app --reload
```

Visit:
- API root → http://127.0.0.1:8000
- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

## 📡 API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET`  | `/` | Health check |
| `POST` | `/user/?username={username}` | Add a GitHub user by username |
| `GET`  | `/users/` | List all stored users |
| `POST` | `/users/{username}/events` | Fetch the user's recent GitHub events and store new ones (de-duplicated) |
| `GET`  | `/users/{username}/events` | Return stored events for a user, newest first |

### Example usage
```bash
# 1. Add a user
curl -X POST "http://127.0.0.1:8000/user/?username=torvalds"

# 2. List users
curl "http://127.0.0.1:8000/users/"

# 3. Fetch and store events (safe to re-run — duplicates are skipped)
curl -X POST "http://127.0.0.1:8000/users/torvalds/events"
# -> {"message": "Saved 30 new events for torvalds; 0 already stored."}

# 4. Get stored events
curl "http://127.0.0.1:8000/users/torvalds/events"
```

## 🗃️ Inspecting the Database
With a local Docker container:
```bash
docker exec -it github_activity_mongo mongosh github-activity-dev
```
Then in the Mongo shell:
```javascript
show collections
db.users.find()
db.events.find().limit(5)
db.events.countDocuments()
```
(For Atlas, use the **Collections** browser in the Atlas UI or connect with `mongosh "<MONGO_URL>"`.)

## 🛠️ Troubleshooting
- **`ServerSelectionTimeoutError`** — MongoDB isn't reachable. For local: is the container up
  (`docker ps`)? For Atlas: is your IP on the Network Access allowlist and the password correct?
- **DNS / SRV errors with `mongodb+srv://`** — ensure `pymongo[srv]` (i.e. `dnspython`) is installed.
- **GitHub `403` rate limit** — set `GITHUB_TOKEN` in `.env`.
- **`User not in database`** when fetching events — add the user with `POST /user/` first.

## 🗺️ Roadmap
This app is evolving from a raw activity tracker into a throughput/effectiveness planner:
- **Metrics API** — aggregation endpoints for throughput, PR cycle time, and activity/streaks
  (built on MongoDB's aggregation pipeline)
- **Dashboard** — a web frontend rendering the metrics as charts and tables
- **Scheduled ingestion** — a local scheduler to refresh user data automatically

## 🙏 Acknowledgments
- FastAPI
- MongoDB / PyMongo
- Docker
- GitHub REST API
