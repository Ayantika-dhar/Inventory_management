

import os
from dotenv import load_dotenv

load_dotenv()

# Fallbacks if not found in .env
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./inventory.db")


