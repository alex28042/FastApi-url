from fastapi import FastAPI
from starlette.responses import RedirectResponse
from pydantic import BaseModel



app = FastAPI()

class url_add(BaseModel):
    url: str
    url_short: str

dic = []

@app.get("/")
async def root():
    return {"message": "Url-shortener"}

@app.get("/urls")
async def url_list():
    return dic

@app.get("/{url_short}")
async def get_url(url_redirect: str):
    if dic.get(url_add.url_short) == url_redirect:
        return RedirectResponse(url = url_add.url)
    else:
        return {"message":"not found"}


@app.post("/url/add")
async def add_url(urls: url_add):
    dic.append(urls)
    return dic[- 1]


@app.get("/redirect")
async def redirect():
    return RedirectResponse('/')

