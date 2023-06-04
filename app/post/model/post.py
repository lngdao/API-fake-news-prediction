from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

class Post(BaseModel):
  title: str
  description: str
  content: str
  image: str
  created_at: datetime