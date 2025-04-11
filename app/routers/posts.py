from typing import List, Optional
from app.models import Post, Votes, User
from app.schemas import PostCreate, PostResponse, PostWithVoteResponse
from fastapi import Response, status, HTTPException, Depends, APIRouter
from app.db import SessionDep, get_session
from sqlmodel import Session
import app.auth.oauth2 as oauth2
from sqlalchemy import func, select, text
from sqlalchemy.orm import joinedload



router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

# Get all posts
@router.get("/", response_model=List[PostResponse])
# @router.get("/", response_model=List[PostWithVoteResponse])
# @router.get("/")
def get_posts(limit: int = 10, skip: int = 0, search: Optional[str] = "", db: Session = Depends(get_session),  current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(Post).filter(Post.title.contains(search)).limit(limit).offset(skip).all()
    # results = (
    #     db.query(Post, func.count(Votes.post_id).label("votes"))
    #     .options(joinedload(Post.owner))
    #     .join(Votes, Votes.post_id == Post.id, isouter=True)
    #     .group_by(Post.id)
    #     .all()
    # )
    # # cursor.execute(SQL_QUERY["GET_ALL_POSTS"])
    # # my_posts = cursor.fetchall()

    # print("--------------------------")
    # result = [{"Post": post.dict(), "votes": votes} for post, votes in results]
    # print(result)
    # print("--------------------------")
    
    return posts 


# Create a post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_session), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(SQL_QUERY["CREATE_POST"], (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # connection.commit()
    new_post = Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# Get post by Id
@router.get("/{id}", response_model=PostResponse)
# @router.get("/{id}", response_model=PostWithVoteResponse)
def get_post_by_id(id: int, db: Session = Depends(get_session),  current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(SQL_QUERY["GET_POST_BY_ID"], (str(id),))
    # post = cursor.fetchone()
    post = db.query(Post).filter(Post.id == id).first()
    # post = (
    #     db.query(Post, func.count(Votes.post_id).label("votes"))
    #     .join(Votes, Votes.post_id == Post.id, isouter=True)
    #     .join(Post.owner)
    #     .group_by(Post.id)
    #     # .options(joinedload(Post.owner))
    #     .filter(Post.id == id).first()
    # )
    print(post)
    
    if not post:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_session),  current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(SQL_QUERY["DELETE_POST_BY_ID"], (str(id),))
    # post = cursor.fetchone()
    # connection.commit()
    post = db.query(Post).filter(Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}', response_model=PostResponse)
def update_post(id: int, post: PostCreate, session: SessionDep,  current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(SQL_QUERY['UPDATE_POST_BY_ID'], (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # connection.commit()
    post_db = session.get(Post, id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post_data = post.model_dump(exclude_unset=True)
    post_db.sqlmodel_update(post_data)
    session.add(post_db)
    session.commit()
    session.refresh(post_db)
    return post_db
