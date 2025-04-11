from fastapi import Depends
# import psycopg2
# from psycopg2.extras import RealDictCursor
from sqlmodel import Field, Session, SQLModel, create_engine  
# import os
from typing import Annotated
from app.config import settings
from sqlalchemy.ext.declarative import declarative_base


DB_URL = settings.DB_URL
HOST = settings.HOST 
DATABASE_NAME = settings.DATABASE_NAME
PASSWORD = settings.DB_PASSWORD
USERNAME = settings.DB_USERNAME 


# def connect_db():
#     try:
#         conn = psycopg2.connect(host=HOST, database=DATABASE_NAME, user=USERNAME, password=PASSWORD, cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection successfully")
#         return {"cursor": cursor, "conn": conn}
#     except Exception as error:
#         print("Database connection failed with ERROR: ", error)
 
 

connection_string = f"{DB_URL}@{HOST}/{DATABASE_NAME}"
engine = create_engine(connection_string)

Base = declarative_base()

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


def get_session():
    with Session(bind=engine, autocommit=False, autoflush=False) as session:
        yield session
        
        
SessionDep = Annotated[Session, Depends(get_session)]


