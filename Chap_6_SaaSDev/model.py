"""
    This module contains the Book class
"""
from pydantic import BaseModel

class Book(BaseModel):
    """
        Book class
    """
    name: str
    author: str
    isbn: str
    price: float = 0.0

book = Book(name="The Pragmatic Programmer", author="Andrew Hunt and David Thomas", isbn="978-0135957059")
print(book)
print(book.name)
