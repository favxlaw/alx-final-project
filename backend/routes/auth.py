from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import Depends
from sqlalchemy.orm import Session 
from datetime import datetime, timedelta
from ..crud import crud
from models.auth import User, Token


from . import  crud, models, schemas
from .database import get_db
from .utils import get_hashed_password, verify_password # Corrected the typo


#  secret key and algorithm for JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Token expiration in minutes
ACCESS_TOKEN_EXPIRE = 25

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Verify user credentials
def verify_credentials(username: str, password: str):
    user = crud.get_user_by_username(username) # Replaced users with crud.get_user_by_username
    if not user or user.password != password:
        return False
    return user 

# Function to create an access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=15) # Renamed expire to expires
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to get the curent user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= "Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(username) # Replaced users with crud.get_user_by_username
    if user is None:
        raise credentials_exception
    return user

# Function to get the current active user from the token
def get_current_active_user(current_user: schemas.User = Depends(get_current_user)): # Changed models.User to schemas.User
     if not current_user.is_active:
         raise HTTPException(status_code=400, details="Inactive user")
     return current_user

# API router
router = APIRouter()

# Token Endpoint
@router.post("/token", response_model=Token)
async def create_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verify_credentials(form_data.username, form_data.password )
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


@router.post("/signup", response_model=schemas.User)
async def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Hash the user's password
    user.hashed_password = get_hashed_password(user.password)
    # Check if the user already exists
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already taken")
    # Create the user in the database
    return crud.create_user(db, user)

@router.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db:
                Session = Depends(get_db)):
    # Verify the username and password
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password") 
    