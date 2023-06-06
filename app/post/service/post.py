from app.post.model.post import Post
from typing import List
import connection
from datetime import datetime
from bson import ObjectId


class PostService:
    def __init__(self):
        ...

    async def get_post_list(self) -> List[Post]:
        data = connection.db["post"].find()
        data = [
            {
                "_id": str(item["_id"]),
                "title": item["title"],
                "image": item["image"],
                "description": item["description"],
                "created_at": item["created_at"],
            }
            for item in data
        ]

        return data

    async def get_post_detail(self, post_id) -> Post:
        post = connection.db["post"].find_one({"_id": ObjectId(post_id)})
        post["_id"] = str(post["_id"])
        post["created_at"] = post["created_at"].isoformat()

        return post

    async def create_post(self, req_data) -> Post:
        result = connection.db["post"].insert_one(
            {
                "title": req_data.title,
                "description": req_data.description,
                "content": req_data.content,
                "created_at": req_data.created_at,
                "image": req_data.image,
            }
        )

        inserted_id = result.inserted_id
        post = Post(
            id=str(inserted_id),
            title=req_data.title,
            description=req_data.description,
            content=req_data.content,
            created_at=req_data.created_at,
            image=req_data.image,
        )

        return post

    async def prediction_post_content(self, req_data) -> Post:
        result = "Tin giả 100% nha quý zị"

        return result
