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

## License

This project is intended for backend development practice and internal use only.
 
