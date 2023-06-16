"""
    This is a simple Hello World application that will be used to demonstrate
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> None:
    """
        This is the main function that will be called when the application is run
        call using localhost:8000
    """
    return "Welcome to the sample fastAPI App!"

@app.get("/hello")
def hello_world() -> None:
    """
        returns Hello World!
        call using localhost:8000/hello
    """
    return "Hello World!"

@app.get("/hello/{name}")
def hello_name(name: str) -> None:
    """
        returns the name passed in the URL 
        call using localhost:8000/hello/<name>
    """
    return f"Hello {name}!"

