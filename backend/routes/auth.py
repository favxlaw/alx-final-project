from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import Depends
from datetime import datetime, timedelta
from schemas import schemas
from models.auth import Token, Config, User, PyObjectId
from config.db import user_collection
from . utils import get_hashed_password, verify_password
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from bson.objectid import ObjectId


#  secret key and algorithm for JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Token expiration in minutes
ACCESS_TOKEN_EXPIRE = 25

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Verify user credentials
async def verify_credentials(username: str, password: str):
    user = await user_collection.find_one({"username": username})
    if not user or not verify_password(password, user["hashed_password"]):
        return False
    return User(**user)

# Function to create an access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to get the current user from the token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await user_collection.find_one({"username": username})
    if user is None:
        raise credentials_exception
    return User(**user)

# Function to get the current active user from the token
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API router
router = APIRouter()

# Token Endpoint
@router.post("/token", response_model=Token)
async def create_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await verify_credentials(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup", response_model=User)
async def signup(user: schemas.UserCreate):
    # Hash the user's password
    user.hashed_password = get_hashed_password(user.password)
    # Check if the user already exists
    db_user = await user_collection.find_one({"username": user.username})
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    db_user = await user_collection.find_one({"email": user.email})
    if db_user:
        raise HTTPException(status_code=400, detail="Email already taken")
    # Create the user in the database
    user.id = await user_collection.insert_one(user.dict(by_alias=True))
    return user

@router.post("/login", response_model=Token)
async def login(current_user: User = Depends(get_current_active_user)):
    # Generate a new access token for the logged in user
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    access_token = create_access_token(
        data={"sub": current_user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}