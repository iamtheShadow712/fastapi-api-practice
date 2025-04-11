from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

    

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class UserCreate(User):
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    username: str
    
    # Converts the object into valid pydantic model
    class Config:
        orm_mode = True
        
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode = True
    
class TokenData(BaseModel):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        orm_mode = True
    
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True 
    
class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse
    content: str
    
    class Config:
        orm_mode = True
        
class PostWithVoteResponse(PostBase):
    Post: PostResponse
    votes: int
    
    class Config:
        orm_mode = True 

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore