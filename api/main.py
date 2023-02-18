from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import settings

users = {"freddy": {"password": "1234"}, "lizbeth": {"password": "1234"}}

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("homepage.html", {"request": request})


class inputLogin(BaseModel):
    username: str
    password: str


@app.post("/login")
async def login(input: inputLogin):
    if input.username not in users:
        return False
    if input.password != users[input.username]["password"]:
        return False
    return True
