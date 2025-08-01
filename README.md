# Inventory Management System - Backend (FastAPI)

This is the backend implementation for an Inventory Management System using **FastAPI**, **PostgreSQL**, and **JWT Authentication**.

## Features

-  Register and authenticate admin users using JWT
-  Add, update, and list products
-  Update product quantity
-  Basic analytics API (e.g., most added products)
-  Swagger-based interactive API docs at `/docs`

## Tech Stack

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **JWT Authentication**
- **Uvicorn**

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/inventory-management-backend.git
   cd inventory-management-backend
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Edit `app/config.py` and set your:
   - `DATABASE_URL`
   - `SECRET_KEY`
   - `ALGORITHM`

5. **Run the App**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access API Docs**
   ```
   http://localhost:8000/docs
   ```

## Folder Structure

```
inventory-management-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   └── user.py, product.py
│   ├── routes/
│   │   └── auth.py, product.py, analytics.py
│   └── schemas/
│       └── user.py, product.py
│
├── requirements.txt
└── README.md
```

## Docker Support

This backend is also Dockerized to simplify deployment.

-  A `Dockerfile` is present in the **root** of the repository to containerize the FastAPI application.
-  The container starts the app on an **insecure HTTP port** using the `PORT` environment variable.

### Build Docker Image

```bash
docker build -t fastapi-backend .
```

### Run the Container

```bash
docker run -d -p 8000:8000 -e PORT=8000 fastapi-backend
```

Visit the app at: `http://localhost:8000`

## License

This project is intended for backend development practice and internal use only.
