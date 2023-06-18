"""
    Dataclass example
"""
from dataclasses import dataclass

@dataclass
class Book():
    """
        Book class
    """
    name: str
    author: str
    isbn: str

dataclass_book = Book("The Pragmatic Programmer", "Andrew Hunt and David Thomas", "978-0135957059")
print(dataclass_book)
print(dataclass_book.name)
print(dataclass_book.author)
print(dataclass_book.isbn)
