SaaS Development Basics (15 minutes):

Briefly explain the concept of SaaS and its advantages.
Discuss common SaaS development frameworks and tools.
Highlight the importance of scalability, security, and user experience.

# FastAPI
- Created in 2018 by [Sebastian Ramirez](https://tiangolo.com/)
- [FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- Other web frameworks are Django, Flask.
- This mini-tutorial will explore upcoming FastAPI only.

- Advantages listed as in website:

The key features are:

> - Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
> - Fast to code: Increase the speed to develop features by about 200% to 300%. *
> - Fewer bugs: Reduce about 40% of human (developer) induced errors. *
> - Intuitive: Great editor support. Completion everywhere. Less time debugging.
> - Easy: Designed to be easy to use and learn. Less time reading docs.
> - Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
> - Robust: Get production-ready code. With automatic interactive documentation.
> - Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

## Basic Package Needs

- `pip install fastapi` The fastAPI Framework
- `pip install uvicorn` The Uvicorn web server - to render the URL on say localhost:<port>
- `pip install requests` The requests synchronous web client
- `pip install httpx` The Httpx syncronous/asynchronous web client package
- `pip install httpie` A simple text web client

## Simple Hello World App

### How to run the application?


- `uvicorn Chap_6_SaaSDev.hello_world:app --reload`
- Note - since `hello_world.py` is under the Folder named `Chap_6_SaasDev`, you need to do the dot notation for the application to locate the basic app.
- The web server automatically is watching for changes to the application files under `'/workspaces/sdlc-python-internship'` and reloads it for you. This is because we used the option `--reload` when using `Uvicorn`

#### Using Browser
- Since you are inside a codespace, the environment figures out the need for a browser and gives you the option to open a browser to interact with the web server running inside the codespace.
- Hence the URL will look funny like `https://codekunoichi-animated-meme-4q5jgpwxxv43qg6p-8000.preview.app.github.dev/hello`
- Instead of `http://127.0.0.1:8000` replace with the browser URL that shows up and use the path decorator accordingly.
- So in our case - the above `http://127.0.0.1:8000` is equivalent to `https://codekunoichi-animated-meme-4q5jgpwxxv43qg6p-8000.preview.app.github.dev/` 
- Append the appropriate path decorators for which you have mapped a function.

#### Using Httpie

```
$ http localhost:8000

HTTP/1.1 200 OK
content-length: 36
content-type: application/json
date: Fri, 16 Jun 2023 15:31:36 GMT
server: uvicorn

"Welcome to the sample fastAPI App!"
```
- With `-b` this will skip the response headers and only print the body.
