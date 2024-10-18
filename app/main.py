from fastapi import FastAPI
from app.routers import books, authors
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API LIBRARY MANAGEMENT", version="0.0.1")

app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(books.router, prefix="/books", tags=["books"])
