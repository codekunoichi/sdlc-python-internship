SaaS Development Basics (15 minutes):

Briefly explain the concept of SaaS and its advantages.
Discuss common SaaS development frameworks and tools.
Highlight the importance of scalability, security, and user experience.

# FastAPI
- Created in 2018 by [Sebastian Ramirez](https://tiangolo.com/)
- [FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- FastAPI supports modern Python asynchronous web standard [ASGI](https://asgi.readthedocs.io/en/latest/)
- Other web frameworks are Django, Flask. They are based on traditional synchronous [WSGI](https://wsgi.readthedocs.io/en/latest/what.html) standard.
- This mini-tutorial will explore upcoming FastAPI only.
- The book [FastAPI](https://learning.oreilly.com/library/view/fastapi/9781098135492/) the early release verion by `Bill Lubanovic` is short, sweet, and effective examples. The following notes are inspired by reading the book June 2023.

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
- You can `cd Chap_6_SaaSDev`
- `uvicorn hello_world:app --reload`

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

```
http -b localhost:8000/ 

"Welcome to the sample fastAPI App!"
```
- Post example
```
$ http -v localhost:8000/greetings who=Mom

POST /greetings HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 14
Content-Type: application/json
Host: localhost:8000
User-Agent: HTTPie/3.2.2

{
    "who": "Mom"
}


HTTP/1.1 200 OK
content-length: 9
content-type: application/json
date: Fri, 16 Jun 2023 20:17:40 GMT
server: uvicorn

"Hi! Mom"
```

## Automatic API Docs!

`http://localhost:8000/docs`

- FastAPI generates an OpenAPI Spec from the path decorators mentioned, swagger document will be generated.
- Since I am inside a codespace, the URL was like `https://codekunoichi-animated-meme-4q5jgpwxxv43qg6p-8000.preview.app.github.dev/docs`
- ![image](https://github.com/codekunoichi/sdlc-python-internship/assets/29447019/a6756cf2-0518-4210-a29f-4adb00782ea8)

## Tiny but Mighty and Cute Web App

- model.py - Your data model
- data.py - Your fake book list
- web.py - Make an end point with 4 lines of code that returns the list of the books! Yay!!


