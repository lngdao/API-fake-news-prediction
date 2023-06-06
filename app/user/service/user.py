from typing import List
import connection
from datetime import datetime
from bson import ObjectId
from fastapi import HTTPException


class UserService:
    def __init__(self):
        ...

    async def get_profile(self, identifier):
        user = connection.db["user"].find_one({"username": identifier})
        
        if not user:
          raise HTTPException(status_code=403, detail="An error occurred") 
        
        profile = {"username": user["username"], "name": user["name"]}

        return profile
