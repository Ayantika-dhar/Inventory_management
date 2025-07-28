import uvicorn
from app.database import Base, engine
from app.models import user, product  # This will create tables for both models

# Create tables in DB
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

