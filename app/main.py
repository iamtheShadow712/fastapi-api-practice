from fastapi import FastAPI 
from app.db import create_db_and_tables
from app.routers import users, posts, auth, vote
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

# db_dict = connect_db()
# cursor = db_dict["cursor"]
# connection = db_dict["conn"]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(vote.router)
