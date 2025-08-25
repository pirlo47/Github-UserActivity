# GitHub User Activity Tracker API

## 📌 Project Overview
This project is a **FastAPI-based REST API** that tracks GitHub users and their activity.  
It fetches user details and recent activity events from the **GitHub REST API**, stores them locally in a database using **SQLAlchemy ORM**, and makes them accessible through REST endpoints.

This can be useful for:
- Tracking contributions of specific GitHub users
- Building activity dashboards
- Learning FastAPI, SQLAlchemy, and API integration

---

## ✨ Key Features
- Fetch and store GitHub user details (`username`, `name`, `avatar_url`)
- Fetch and store user activity events (`event type`, `repo name`, `timestamp`)
- SQLite database (can be swapped for PostgreSQL/MySQL)
- Auto-generated API docs with **Swagger UI** at `/docs`
- RESTful endpoints for:
  - Adding a GitHub user
  - Listing users
  - Fetching and storing events
  - Viewing stored events

---

## 📂 Project Structure
```
.
├── main.py           # FastAPI application with endpoints
├── database.py       # Database setup & ORM models (User, Event)
├── requirements.txt  # Python dependencies
├── useractivity.db   # SQLite database (auto-created after first run)
└── README.md         # Project documentation
```

---

## 🔧 Prerequisites
Before running the application, ensure you have:
- **Python 3.9+** installed
- **pip** (Python package manager)
- (Optional) **GitHub Personal Access Token** if you expect to make many requests (to avoid GitHub API rate limits)

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-project-folder>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

---

## 🚀 Running the Application

Once started, the app will run at:  
http://127.0.0.1:8000/

Interactive API documentation available at:  
- Swagger UI: http://127.0.0.1:8000/docs  
- ReDoc: http://127.0.0.1:8000/redoc

---

## 📡 Usage Examples

### 1. Add a GitHub User

**cURL**
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"username": "octocat"}'
```

**Postman**
- Method: POST
- URL: http://127.0.0.1:8000/users/
- Body → raw → JSON:
```json
{
  "username": "octocat"
}
```

### 2. List All Users

**cURL**
```bash
curl -X GET "http://127.0.0.1:8000/users/"
```

**Postman**
- Method: GET
- URL: http://127.0.0.1:8000/users/

### 3. Fetch and Save Events for a User

**cURL**
```bash
curl -X POST "http://127.0.0.1:8000/users/octocat/events"
```

**Postman**
- Method: POST
- URL: http://127.0.0.1:8000/users/octocat/events

### 4. Get Events for a User

**cURL**
```bash
curl -X GET "http://127.0.0.1:8000/users/octocat/events"
```

**Postman**
- Method: GET
- URL: http://127.0.0.1:8000/users/octocat/events

---

## 🛠️ Troubleshooting Common Issues

**sqlite3.OperationalError: unable to open database file**
- Make sure your DATABASE_URL in database.py is `sqlite:///./useractivity.db` (with `./`, not `////`).
- Ensure the app has permission to write in the current directory.

**404 Not Found when adding users**
- You must send a POST request to `/users/` with JSON body:
```json
{
  "username": "octocat"
}
```

**GitHub API rate limit exceeded (403)**
- GitHub allows 60 unauthenticated requests/hour.
- To increase the limit, use a GitHub Personal Access Token in your requests.
  Example:
  ```python
  headers = {"Authorization": "token YOUR_PERSONAL_ACCESS_TOKEN"}
  requests.get(url, headers=headers)
  ```

---

## 🙏 Acknowledgments

- FastAPI for the web framework
- SQLAlchemy for ORM/database management
- GitHub REST API for user and event data
- You 🎉 for building and extending this project!
headers = {"Authorization": "token YOUR_PERSONAL_ACCESS_TOKEN"}
requests.get(url, headers=headers)
🙏 Acknowledgments
FastAPI for the web framework

SQLAlchemy for ORM/database management

GitHub REST API for user and event data



