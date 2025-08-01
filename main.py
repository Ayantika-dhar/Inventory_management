'''import uvicorn
from app.database import Base, engine
from app.models import user, product  # This will create tables for both models

# Create tables in DB
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)'''

'''from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models import user, product
from app.routes import auth, product as product_routes

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI()

# CORS middleware (allowing frontend at localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])

# Optional: Root endpoint
@app.get("/")
def root():
    return {"message": "Inventory Management API is running."}'''


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models import user, product
from app.routes import auth, product as product_routes
import os
import uvicorn

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Configure CORS (allow frontend at localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include route modules
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Inventory Management API is running."}

# Run the app on a port defined by the PORT environment variable
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)



