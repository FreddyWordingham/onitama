from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from . import settings

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("homepage.html", {"request": request})
