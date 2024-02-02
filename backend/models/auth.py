from pydantic import BaseModel, Field, GetJsonSchemaHandler
from typing import Optional, ClassVar, Any, Dict 
from datetime import datetime
from pydantic_core import CoreSchema 
from bson.objectid import ObjectId

from fastapi.security import OAuth2PasswordBearer

# Response model
class ResponseModel(BaseModel):
    detail: str

# Error response model
class ErrorResponseModel(BaseModel):
    message: str
    status_code: int
    error: str

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


def get_user(username: str) -> Optional[User]:
        return User.users.get(username)
    
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> Dict[str, Any]:
        json_schema = super().__get_pydantic_json_schema__(core_schema, handler)
        json_schema = handler.resolve_ref_schema(json_schema)
        json_schema.update(type="string")
        return json_schema

# the User and Token models to use the PyObjectId class
class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    hashed_password: str = Field(...)
    is_active: bool = Field(...)

class Config:
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    allow_population_by_field_name = True
          
            
    

