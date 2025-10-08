# 🚀 GitHub User Activity Tracker API

## 📌 Project Overview
This is a FastAPI-based REST API that tracks GitHub users and their activity. It fetches user details and recent events from the GitHub REST API, stores them in PostgreSQL via SQLAlchemy, and exposes them through REST endpoints.

Perfect for:
- Tracking GitHub users’ contributions
- Building activity dashboards
- Learning FastAPI, SQLAlchemy, and PostgreSQL integration

## ✨ Key Features
- Fetch and store GitHub user details (username, name, avatar_url)
- Fetch and store user activity events (event type, repo name, timestamp)
- PostgreSQL DB with SQLAlchemy
- Environment-based DB config (.env)
- Database migrations with Alembic
- Auto-generated API docs (Swagger UI)
- REST endpoints to add users, list users, fetch/save events, and retrieve stored events

## 📂 Project Structure
```
.
├── main.py             # FastAPI app and endpoints
├── database.py         # DB setup, ORM models (User, Event)
├── migrations/         # Alembic migration scripts
├── docker-compose.yml  # Docker setup for PostgreSQL
├── .env                # Environment variables (DB connection)
├── requirements.txt    # Python dependencies
└── README.md
```

## 🔧 Prerequisites
- Python 3.9+
- Docker & Docker Compose
- pip
- (Optional) GitHub Personal Access Token to avoid API rate limits

## ⚙️ Environment Configuration
Create a `.env` file in the project root with the database URL:

```bash
# .env
DATABASE_URL=postgresql+psycopg2://app_user:app_password@localhost:5432/github_activity
```

This URL is used by both FastAPI and Alembic to connect to PostgreSQL.

## 🐳 Docker Setup (PostgreSQL + pgAdmin)
Start containers:
```bash
docker compose up -d
```

Verify:
```bash
docker ps
```

### pgAdmin (optional)
Open: http://localhost:5050  
Login: admin@local.com / admin

Add a new server → Connection:
- Host: db
- Port: 5432
- Username: app_user
- Password: app_password

## 🧠 Database Setup with Alembic
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run migrations:
```bash
alembic upgrade head
```

## 🧩 Running the FastAPI Server
Start the API server:
```bash
uvicorn main:app --reload
```

Visit:
- API Root → http://127.0.0.1:8000
- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

## 📡 Example Usage
1. Add a GitHub User
```bash
curl -X POST "http://127.0.0.1:8000/user/?username=octocat"
```
2. List All Users
```bash
curl -X GET "http://127.0.0.1:8000/users/"
```
3. Fetch and Save Events
```bash
curl -X POST "http://127.0.0.1:8000/users/octocat/events"
```
4. Get Saved Events
```bash
curl -X GET "http://127.0.0.1:8000/users/octocat/events"
```

## 🗃️ Accessing PostgreSQL Directly
Open Postgres shell in the container:
```bash
docker exec -it github_activity_db psql -U app_user -d github_activity
```

Useful commands:
```
\dt
SELECT * FROM users;
SELECT * FROM events LIMIT 5;
```

Export a backup:
```bash
docker exec -t github_activity_db pg_dump -U app_user github_activity > backup.sql
```

## 🛠️ Troubleshooting
- Password authentication failed: ensure `.env` matches Docker credentials. To reset:
```bash
docker compose down -v && docker compose up -d
```
- Database not found: run `alembic upgrade head`
- API not connecting: ensure PostgreSQL container is running (`docker ps`)

## 🙏 Acknowledgments
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker
- pgAdmin
- GitHub REST API