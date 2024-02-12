import secrets 
import hashlib
from typing import Optional
from pydantic import BaseModel
from models.auth import User, get_user
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


# Define constants
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 25
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to hash a password
def get_hashed_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify a password
def verify_password(password: str, hashed_password: str):
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password

users = {}

# Function to create a user and save it to the database
def create_user(username: str, password: str, is_active: bool) -> User:
# Check if the username is already taken
    if username in users:
        raise ValueError("Username already exists")
# Create a user object
    user = User(username=username, password=password, is_active=is_active)
# Save the user object to the users dictionary
    users[username] = user
    return user

#Function to get a user by username
def update_user (username: str, password: Optional[str] = None, is_active:
                 Optional[bool] = None) -> User:
        user = get_user(username)
        if user is None:
            raise ValueError("User not found")
        if password is not None:
            user.password = password
        if is_active is not None:
            user.is_active = is_active
        return user

# Function to delete a user by username
def delete_user(username: str) -> None:
    # Get the user object by username
    user = get_user(username)
    # If the user does not exist, raise an error
    if user is None:
        raise ValueError("User not found")
    # Delete the user object from the users dictionary
    del users[username]

# Function to create a token for a user by username
def create_token(username: str) -> str:
    # Get the user object by username
    user = get_user(username)
    # If the user does not exist or is not active, raise an error
    if user is None or not user.is_active:
        raise ValueError("User not found or inactive")
    # Generate a random token
    token = secrets.token_hex(16)
    # Save the token to the user object
    user.token = token
    # Return the token
    return token

# Function to get a user by token
def get_user_by_token(token: str) -> Optional[User]:
    # Loop through the users dictionary
    for user in users.values():
        # If the user has the given token, return the user object
        if user.token == token:
            return user
    # If no user has the given token, return None
    return None