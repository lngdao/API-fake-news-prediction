from app.post.model.post import Post
from typing import List
import connection
from datetime import datetime

class PostService:
  def __init__(self):
    ...

  async def get_post_list(self) -> List[Post]:
    data = connection.db["post"].find()
    data = [{"_id": str(item["_id"]), "title": item["title"], "image": item["image"], "description": item["description"], "content": item["content"], "created_at": item["created_at"]} for item in data]

    return {"message": "success", "data": data}