from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def MostrarInicio(request: Request):
    return  templates.TemplateResponse("index.html", {"request": request})

@app.get("/Contactanos", response_class=HTMLResponse)
def MostrarContactanos(request: Request):
    return templates.TemplateResponse("Contactanos.html", {"request": request})