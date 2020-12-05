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

class User_in_db(User):
    db_password: str

dic = []
fake_users_db = {}

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User_in_db(**user_dict)
    
def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user
    

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@app.post("/login")
async def login(from_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_date.username)
    user = User_in_db(**user_dict)
    db_password = fake_hash_password(form_data.password)

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/")
async def root():
    return {"message": "Url-shortener"}

@app.get("/urls")
async def url_list(token: str = Depends(oauth2_scheme)):
    return dic

@app.get("/{url_short}")
async def get_url(shorten: str):
    for i in dic:
        if i.short == shorten:
            return RedirectResponse(i.url)

@app.post("/url/add")
async def add_url(item: url_add):
    if item.url_short == 0:
        item.url_short = str
    dic.append(item)
    return item


@app.get("/redirect")
async def redirect():
    return RedirectResponse('/')

