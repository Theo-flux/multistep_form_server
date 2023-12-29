from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from settings import mongodb_uri, db_name
from models import FormModel


app = FastAPI(
    title="Multistep Form server",
    description="A Multistep Form API Service.",
    summary="Frontendmentors: Multistep form challenge.",
    version="0.0.1",
    contact={
        "name": "Theo Flux",
        "url": "http://www.github.com/Theo-flux",
        "email": "tifluse@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt",
    },
)

origins = ["http://localhost:5173", "https://multistep-form-client.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_db_client():
    # on event startup, connect to the mongodb client
    try:
        app.mongodb_client = AsyncIOMotorClient(mongodb_uri)
        app.mongodb = app.mongodb_client[db_name]
        app.mongodb_status = "connected to database"
    except Exception as e:
        app.mongodb_status = "unable to connect to database"


@app.on_event("shutdown")
async def shudown_db_client():
    app.mongodb_client.close()


@app.get("/", tags=["Welcome"])
async def welcome(request: Request):
    connection_status = request.app.mongodb_status
    return {
        "message": "Welcome to my Multistep Form API Service",
        "database_status": connection_status,
    }


@app.post("/form", tags=["Subscription form"])
async def step_form_post(request: Request, form_data: FormModel = Body(...)):
    request.app.mongodb
    return {"msg": "subscription form", "data": form_data}
