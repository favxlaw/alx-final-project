from pydantic import BaseModel
from typing import Optional, ClassVar
from datetime import datetime

# User Model
class User(BaseModel):
    username: str
    password: str
    is_active: bool
    users: ClassVar[dict] = {} # database

# Token Model
class Token(BaseModel):
        access_token: str
        token_type: str
        expires_at: Optional[datetime]
        tokens: ClassVar[dict] = {} # database

# Function to create, update, delete, and query users and tokens
def create_user(username: str, password: str, is_active:bool) -> User:
        # Checking sth create a user and save it to the database
        user = User(username=username, password=password, is_active=is_active)
        User.users[username] = user # using class name to access the class variable
        return user
    
def get_user(username: str) -> Optional[User]:
        return User.users.get(username)
    
        
            
    

