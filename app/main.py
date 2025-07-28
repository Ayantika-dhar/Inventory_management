from fastapi import FastAPI
from app.routes import auth, product

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(product.router, prefix="/products", tags=["Products"])

@app.get("/")
def root():
    return {"message": "Inventory Management System API"}

