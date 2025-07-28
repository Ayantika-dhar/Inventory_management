'''from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.database import SessionLocal
from app.auth import get_current_user  # ✅ Import for token validation

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProductResponse)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/", response_model=List[ProductResponse])
def get_products(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return db.query(Product).all()


@router.put("/{product_id}/quantity", response_model=ProductResponse)
def update_quantity(
    product_id: int = Path(..., description="The ID of the product to update"),
    payload: ProductUpdate = Depends(),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.quantity = payload.quantity
    db.commit()
    db.refresh(product)
    return product'''


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse, ProductQuantityUpdate
from app.database import SessionLocal
from app.auth import get_current_user




router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProductResponse)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product




@router.get("/", response_model=List[ProductResponse])
def get_products(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, gt=0, le=100, description="Max number of items to return"),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return db.query(Product).offset(skip).limit(limit).all()

@router.get("/analytics/most-added", response_model=List[ProductResponse])
def get_most_added_products(
    limit: int = Query(5, ge=1),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return db.query(Product).order_by(Product.quantity.desc()).limit(limit).all()

@router.put("/{product_id}/quantity", response_model=ProductResponse)
def update_quantity(
    product_id: int,
    update: ProductQuantityUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.quantity = update.quantity
    db.commit()
    db.refresh(product)
    return product





