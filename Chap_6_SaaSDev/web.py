"""
    This file contains the FastAPI code demoing basic wiring of data.py, model.py, and web.py
"""
from model import Book
from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/books")
def get_books() -> list[Book]:
    """
        Returns the list of books
    """
    from data import get_books  
    return get_books()