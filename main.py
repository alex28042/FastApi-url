import enum
from typing import Coroutine
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from enum import Enum



app = FastAPI()

class url_names(str, Enum):
    core = "core"

@app.get("/")
async def root():
    return {"message": "Url-shortener"}

@app.get("/url-list")
async def url_list(list: url_names):
    return list

@app.get("/url-list/{url}")
async def get_url(url: url_names):
    if url.value == "core":
        return {"message":"https://github.com/orgs/CoreDumped-ETSISI/teams/academy-2020-web-engineering"}

@app.get("/redirect")
async def redirect():
    return RedirectResponse('/')

