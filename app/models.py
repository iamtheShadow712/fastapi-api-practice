from typing import List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, String
from sqlalchemy.sql import expression
from app.db import Base
# from sqlalchemy.ext.declarative import declarative_base




# Base = declarative_base()
    
class User(SQLModel, table=True, metadata=Base.metadata):
    __tablename__ = "users"
    id: int              = Field(primary_key=True, nullable=False)
    username: str        = Field(nullable=False)
    email: str           = Field(nullable=False, unique=True)
    password: str        = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), nullable=False, server_default=expression.func.now()))
    phone_number: str    = Field(sa_column=Column(String, nullable=True)) 
    posts: List["Post"] = Relationship(back_populates="owner")
   
class Post(SQLModel, table=True, metadata=Base.metadata):
    __tablename__ = "posts"
    
    id: int              = Field(primary_key=True, nullable=False)
    title: str           = Field(nullable=False)
    content: str         = Field(nullable=False)
    published: bool      = Field(sa_column=Column(Boolean, nullable=False, server_default=expression.true()))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), nullable=False, server_default=expression.func.now()))
    owner_id: int        = Field(foreign_key="users.id", nullable=False, ondelete="CASCADE")
    owner: "User" = Relationship(back_populates="posts")


class Votes(SQLModel, table=True, metadata=Base.metadata):
    __tablename__ = "votes"
    
    user_id: int        = Field(primary_key=True, foreign_key="users.id", ondelete="CASCADE")
    post_id: int        = Field(primary_key=True, foreign_key="posts.id", ondelete="CASCADE")