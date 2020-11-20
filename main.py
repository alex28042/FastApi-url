from fastapi import FastAPI
from starlette.responses import RedirectResponse
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class url_add(BaseModel):
    url: str
    url_short: str

@app.get("/")
async def root():
    return {"message": "Url-shortener"}

@app.get("/urls")
async def url_list(urls: url_add):
    return urls

@app.post("/url-list")
async def add_url(urls: url_add):
    return urls

@app.get("/url-list/{urls}")
async def get_url(urls: url_add):
    if urls.value == "core":
        return RedirectResponse(url = 'https://github.com/orgs/CoreDumped-ETSISI/teams/academy-2020-web-engineering')

@app.get("/redirect")
async def redirect():
    return RedirectResponse('/')

