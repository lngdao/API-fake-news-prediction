from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

class Post(BaseModel):
  id: str
  title: str
  description: str
  content: str
  image: str
  created_at: datetime