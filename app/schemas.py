from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


# USER SCHEMAS

class UserBase(BaseModel):
    email: EmailStr
    password: str

class CreateUser(UserBase):
    pass 

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None


# POST schemas

class PostBase(BaseModel): 
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at : datetime
    # owner_id: int
    owner: UserOut
        
    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post  # ton schema de Post déjà existant
    votes: int

    class Config:
        from_attributes = True

## Vote

class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1) # type: ignore