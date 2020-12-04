from typing import Optional
from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

class url_add(BaseModel):
    url: str
    url_short: str

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

dic = []
fake_users_db = {}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

def fake_decode_token(token):
    return User(username = token + "fakedecoded", email = "john@example.com", full_name = "Alex")

@app.get("/")
async def root():
    return {"message": "Url-shortener"}

@app.get("/urls")
async def url_list(token: str = Depends(oauth2_scheme)):
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

