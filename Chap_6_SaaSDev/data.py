from model import Book

_books = [  Book(name="The Pragmatic Programmer", author="Andrew Hunt and David Thomas", isbn="978-0135957059"), Book(name="FastAPI", author="Bill Lubanovic", isbn="000-0000000000")]

def get_books() -> list[Book]:
    """
        Returns the list of books
    """
    return _books

print(get_books())