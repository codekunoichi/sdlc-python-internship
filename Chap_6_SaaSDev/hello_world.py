"""
    This is a simple Hello World application that will be used to demonstrate
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> None:
    """
        This is the main function that will be called when the application is run
    """
    return "Welcome to the sample fastAPI App!"

@app.get("/hello")
def hello_world() -> None:
    """
        This is the main function that will be called when the application is run
    """
    return "Hello World!"
