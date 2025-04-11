from dotenv import load_dotenv
# import os
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
   HOST: str
   DATABASE_NAME: str
   DB_URL: str
   DB_PASSWORD: str
   DB_USERNAME: str 
   SECRET_KEY: str
   ALGORITHM: str
   ACCESS_TOKEN_EXPIRE_MINUTES: int 
   
   class Config:
        env_file = ".env"
    
settings = Settings()

# DB_CONFIG = {
#     "HOST": os.getenv('HOST'),
#     "DATABASE_NAME": os.getenv('DATABASE_NAME'),
#     "DB_URL": os.getenv('DB_URL'),
#     "PASSWORD": os.getenv('DB_PASSWORD'),
#     "USERNAME": os.getenv('DB_USERNAME'),
# }
# AUTH_CONFIG = {
#     "SECRET_KEY": os.getenv('SECRET_KEY'),
#     "ALGORITHM": os.getenv('ALGORITHM'),
#     "ACCESS_TOKEN_EXPIRE_MINUTES": os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'), 
# }
