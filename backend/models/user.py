from pydantic import BaseModel, Field, constr, root_validator, ValidationError, EmailStr
from typing import Optional, List
from typing_extensions import Literal
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator
import re

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20)

    @validator('password')
    def password_format(cls, v):
        if not re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", v):
            raise ValueError('Password must contain at least one lowercase letter, one uppercase letter, one digit, and be at least 8 characters long')
        return v
        
    
# Error response model
class ErrorResponseModel(BaseModel):
    message: str
    status_code: int
    error: str
        
class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str
    password: str

class UserResponse(BaseModel):
    id: str 
    name: str
    email: str
    role: str 

