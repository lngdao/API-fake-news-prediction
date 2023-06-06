from typing import List
import connection
from datetime import datetime
from bson import ObjectId
from fastapi import HTTPException
from security import permission


class AuthService:
    def __init__(self):
        ...

    async def register(self, req_data):
        user = connection.db["user"].find_one({"username": req_data.username})

        if user:
            raise HTTPException(status_code=403, detail="Username already exists")

        token = permission.generate_token(username=req_data.username, isAdmin=False)
        user = connection.db["user"].insert_one(
            {
                "username": req_data.username,
                "password": req_data.password,
                "name": req_data.name,
                "isAdmin": False,
                "token": token,
            }
        )

        return token

    async def login(self, req_data):
        user = connection.db["user"].find_one({"username": req_data.username})

        if not user or (user and user["password"] != req_data.password):
            raise HTTPException(status_code=403, detail="Incorrect account or password")
        print(user["isAdmin"])
        token = permission.generate_token(
            username=req_data.username, isAdmin=user["isAdmin"]
        )
        connection.db["user"].update_one(
            {"username": req_data.username}, {"$set": {"token": token}}
        )

        return token
