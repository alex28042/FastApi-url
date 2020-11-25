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
async def get_url(shorten: str):
    for i in dic:
        if url_add.url_short[i] == shorten:
            return RedirectResponse(url_add.url_short[i])



@app.post("/url/add")
async def add_url(item: url_add):
    if item.url_short == 0:
        item.url_short = str
    dic.append(item)
    return item



@app.get("/redirect")
async def redirect():
    return RedirectResponse('/')

