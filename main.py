from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from typing import Optional, List
from starlette import status
app = FastAPI()

class Book (BaseModel):
    author: str
    title: str 
    content: str 
    

book_db = []

@app.get("/ping", status_code=status.HTTP_200_OK)
def root():
    return {"message" :"pong"}

@app.get("/home")
def catch_all():
    with open("welcome.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def add_book(new_book: List[Book]):
    book_db.extend(new_book)
    return book_db

@app.get("/posts", status_code=status.HTTP_200_OK)
def root():
    return book_db

@app.put("/posts")
def update_or_create_book(title: str):
    for i, book in enumerate(book_db):
        if book.title==title:
            book_db[i] = book 
        book_db.append(title)
    return book_db

