from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app import models, schemas

def create_author(db: Session, author: schemas.AuthorCreate):
    if not author.name:
        return JSONResponse(status_code=400, content={"id": 0})
    
    check_exists = db.query(models.Author).filter(models.Author.name == author.name).first()
    if check_exists:
        return JSONResponse(status_code=409, content={"id": check_exists.id})


    db_author = models.Author(name=author.name, bio=author.bio, birth_date=author.birth_date)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()

def delete_author(db: Session, author_id: int):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
        return db_author
    return None

def update(db: Session, author_id: int, author: schemas.AuthorCreate):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author:
        db_author.name = author.name
        db.commit()
        db.refresh(db_author)
        return db_author
    return None