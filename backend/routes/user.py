from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

users = []

@router.post("/users/", response_model=User)
async def create_user(user: User):
    users.append(user)
    return user

@router.get("/users/", response_model=List[User])
async def read_users():
    return users

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    for i, u in enumerate(users):
        if u.id == user_id:
            users[i] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/users/roles/{role}", response_model=List[User])
async def read_users_by_role(role: str):
    return [user for user in users if user.role == role]