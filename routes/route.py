from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated
from sqlalchemy.orm import Session
from models.model import User, Post
from schemas.schema import UserBase, PostBase
from database.connection import SessionLocal
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/user")
async def createUser(user:UserBase, db:db_dependency):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()

@router.get('/user')
async def fetchAllUsers(db:db_dependency):
    return db.query(User).all()

@router.get('/user/{id}')
async def findUserById(id:int, db:db_dependency):
    user =  db.query(User).filter(User.id==id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found!")
    return user



@router.post("/post")
async def createPost(post:PostBase, db:db_dependency):
    db_post = User(**post.dict())
    db.add(db_post)
    db.commit()

@router.get('/post')
async def fetchAllPosts(db:db_dependency):
    return db.query(Post).all()

@router.get('/post/{id}')
async def findPostById(id:int, db:db_dependency):
    post =  db.query(Post).filter(Post.id==id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post Not Found!")
    return post

@router.delete('/post/{id}')
async def deletePost(db:db_dependency):
    post =  db.query(Post).filter(Post.id==id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post Not Found!")
    db.delete(post)
    db.commit()
