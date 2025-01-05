from pydantic import BaseModel
from datetime import datetime
from typing import List

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    timestamp: datetime
    
class Post(BaseModel):
    id: int
    userId: int
    title: str
    body: str
    
class UserPosts(BaseModel):
    posts: List[Post]
    timestamp: datetime