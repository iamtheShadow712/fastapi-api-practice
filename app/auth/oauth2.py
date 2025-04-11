import jwt
from datetime import datetime, timedelta 
from app.schemas import TokenData
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from app.db import SessionDep
from app.models import User
from app.config import settings

# SECRET_KEY - use the following command(openssl rand -hex 32)
# ALGORITHM
# EXPIRATION TIME

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


oauth_scheme = OAuth2PasswordBearer(tokenUrl= "auth/login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return access_token


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if not user_id:
            raise credentials_exception
        token_data = TokenData(id=user_id)
    except jwt.PyJWKError:
        raise credentials_exception
    
    return token_data
    
    
def get_current_user(session: SessionDep, token: str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentials_exception=credentials_exception)
    
    user = session.get(User, token.id)
    return user