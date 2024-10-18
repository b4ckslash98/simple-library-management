from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from ..services.books import create_book, get_books, get_one, update, delete, get_list_by_author

router = APIRouter()

@router.post("/{author_id}/", response_model=schemas.Book)
def create_book_for_author(author_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, book=book, author_id=author_id)

@router.get("/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_books(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Book)
def get_book(id: int, db: Session = Depends(get_db)):
    return get_one(db=db, id=id)

@router.put("/{id}", response_model=schemas.BookUpdate)
def update_books(id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    try:
        exists_book = get_one(db,  id=id)
        if not exists_book:
            raise HTTPException(status_code=404, detail="Book not found")
        process = update(db=db, id=id, book=book)
        return process
    except Exception as e:
        raise HTTPException(status_code=500,  detail=str(e))

@router.delete("/{id}", response_model=schemas.BookBase)
def delete_books(id: int, db: Session = Depends(get_db)):
    return delete(db=db, id=id)

@router.get("/by-author/{author_id}", response_model=List[schemas.Book])
def get_by_author(author_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_list_by_author(db,  author_id=author_id, skip=skip, limit=limit)
