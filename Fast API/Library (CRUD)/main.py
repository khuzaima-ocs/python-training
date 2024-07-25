from typing import Optional
from fastapi import FastAPI
from library import Library

app = FastAPI()

lib = Library()

@app.get('/')
def index():
    return "Welcome to Library Management Sysem"

@app.get('/books')
def get_book_titles():
    return lib.get_book_titles()

@app.post("/add-book")
def add_book(title, author, content):
    lib.add_new_book(title, author, content)
    return {
        "message": "Book added successfully"
    }

@app.get('/book/{title}')
def get_book_details(title):
    response = lib.get_book(title.lower())
    return response

@app.put('/edit-book/{title}')
def edit_book(title: str, new_title: Optional[str] = "", new_author: Optional[str] = "" ,new_content: Optional[str] = ""):
    return lib.edit_book(title.lower(), new_title, new_author ,new_content)

@app.delete('/delete-book/{title}')
def delete_book(title: str):
    return lib.delete_book(title.lower())