from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="User Management API")


class User(BaseModel):
    id: int
    name: str
    phone_no: str
    address: str

class UserUpdate(BaseModel):
    name: str
    phone_no: str
    address: str


users_db = {}


@app.post("/users/", status_code=201)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    
    users_db[user.id] = user
    return {"message": "User created successfully"}


@app.get("/users/search", response_model=List[User])
def search_users(name: str = Query(..., description="Name to search for")):
    matching_users = [user for user in users_db.values() if name.lower() in user.name.lower()]
    return matching_users


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return users_db[user_id]





@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    
    current_user = users_db[user_id]
    updated_user = User(
        id=current_user.id,
        name=user_update.name,
        phone_no=user_update.phone_no,
        address=user_update.address
    )
    
    users_db[user_id] = updated_user
    return {"message": "User updated successfully"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    del users_db[user_id]
    return {"message": "User deleted successfully"}


@app.get("/")
def read_root():
    return {"message": "User Management API is running"}