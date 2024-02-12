from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List


class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20)
    
    
class UserSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    profile_picture: Optional[str] = None
    enrolled_courses: List[str] = Field(default_factory=list)

# Define the update user schema
class UpdateUserSchema(BaseModel):
    username: Optional[str]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    profile_picture: Optional[str]
    enrolled_courses: Optional[List[str]]

