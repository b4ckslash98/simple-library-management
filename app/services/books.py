from sqlalchemy.orm import Session
from app import models, schemas

def create_book(db: Session, book: schemas.BookCreate, author_id: int):
    db_book = models.Book(**book.dict(), author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_one(db: Session,  id: int):
    return db.query(models.Book).filter(models.Book.id == id).first()

def update(db: Session, id: int, book: schemas.BookUpdate):
    db_book = db.query(models.Book).filter(models.Book.id == id).first()
    if db_book:
        db_book.title = book.title
        db_book.author_id = book.author_id
        db.commit()
        db.refresh(db_book)
        return db_book
    return None

def delete(db: Session, id: int):
    db_book = db.query(models.Book).filter(models.Book.id == id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return db_book
    return None

def get_list_by_author(db: Session, author_id: int, skip: int=0, limit: int=10):
    return db.query(models.Book).filter(models.Book.author_id == author_id).offset(skip).limit(limit).all()