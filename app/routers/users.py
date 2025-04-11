from app.models import User
from app.schemas import UserCreate, UserResponse
from fastapi import status, HTTPException, APIRouter, Depends
from app.utils import hash_password
from app.db import SessionDep
from app.auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, session: SessionDep):
    
    # Hash the password
    user.password = hash_password(user.password)
    
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get('/{id}', response_model=UserResponse)
def get_user(id: int, session: SessionDep, current_user = Depends(get_current_user)):
    # user = session.query(models.User).filter(models.User.id == id).first()
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exists")
    return user
    