from pydantic import BaseModel
from datetime import datetime, date
from typing import List, Optional

class BookBase(BaseModel):
    title: str
    description: str
    publis_date: datetime

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    author_id: int

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True

class AuthorBase(BaseModel):
    name: str
    bio: str
    birth_date: date

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List[Book] = []

    class Config:
        from_attributes = True

class AuthorDelete(BaseModel):
    status: str
    message: str