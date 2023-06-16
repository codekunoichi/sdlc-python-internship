"""
    This is a simple Hello World application that will be used to demonstrate fastAPI simplicity
"""
from fastapi import FastAPI, Body

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

@app.get("/greetings")
def greetings(who: str) -> None:
    """
        Illustrates the use of query parameters
        returns Hi!
        call using localhost:8000/hi
    """
    return f"Hi! {who}"

@app.post("/greetings")
def greetings_post(who: str = Body(embed=True)):
    """
        Illustrates the use of Body parameters
        returns Hi!
        call using localhost:8000/hi
    """
    return f"Hi! {who}"