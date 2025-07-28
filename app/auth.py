from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config import SECRET_KEY, ALGORITHM
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# API Key header
token_scheme = APIKeyHeader(name="Authorization", auto_error=True)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(token_scheme)):
    if not token.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid token format")
    token = token.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid or expired token")


