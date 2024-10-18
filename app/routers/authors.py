from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from ..services.authors import create_author as s_create_author, get_author, get_authors, delete_author as s_delete_author, update

router = APIRouter()

@router.post("/", response_model=schemas.Author, status_code=201)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return s_create_author(db=db, author=author)

@router.get("/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_authors(db, skip=skip, limit=limit)

@router.get("/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = get_author(db, author_id=author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.delete("/{author_id}", response_model=schemas.AuthorDelete)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    try:
        author = get_author(db, author_id=author_id)
        if not author:
            raise HTTPException(status_code=404, detail="Author not found")
        s_delete_author(db=db, author_id=author_id)
        return schemas.AuthorDelete(status="success", message="Author deleted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

@router.put("/{author_id}", response_model=schemas.AuthorCreate)
def update_author(author_id: int, author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    try:
        exists_author = get_author(db, author_id=author_id)
        if not exists_author:
            raise HTTPException(status_code=404, detail="Author not found")
        process = update(db=db, author_id=author_id,  author=author)
        return process
    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)