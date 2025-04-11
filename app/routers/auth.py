from fastapi import APIRouter, status, HTTPException, Response, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.db import SessionDep
from app.schemas import Token
from app.models import User
from app.utils import verify_password
from app.auth.oauth2 import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)

@router.post('/login', response_model=Token)
def login(session: SessionDep, user_credentials: OAuth2PasswordRequestForm = Depends()):
    user = session.query(User).filter(User.email == user_credentials.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    is_valid_password = verify_password(user_credentials.password, user.password)
    if not is_valid_password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    # create token
    access_token =  create_access_token(data={"user_id": user.id})
    # return token
    return {"access_token": access_token, "token_type": "bearer"}