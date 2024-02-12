from pydantic import BaseModel, Field, GetJsonSchemaHandler
from typing import Optional, ClassVar, Any, Dict 
from datetime import datetime
from pydantic_core import CoreSchema 
from bson.objectid import ObjectId
from pydantic_core import core_schema


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
    
class PyObjectId(str):
    @classmethod
    def __get_pydantic_core_schema__(
            cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.chain_schema([
                    core_schema.str_schema(),
                    core_schema.no_info_plain_validator_function(cls.validate),
                ])
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x)
            ),
        )

    @classmethod
    def validate(cls, value) -> ObjectId:
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")

        return ObjectId(value)


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
          
            
    

