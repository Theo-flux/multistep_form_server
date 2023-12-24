from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from settings import mongodb_uri, port


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
client = MongoClient(mongodb_uri, port, server_api=ServerApi("1"))


def ping_database():
    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        msg = "Pinged your deployment. You successfully connected to MongoDB!"
        print(msg)
        return "connected to database!"
    except Exception as e:
        print(e)
        return "unable to connect to database!"


ping_database()


@app.get("/", tags=["Welcome"])
async def welcome():
    connection_status = ping_database()
    return {
        "message": "Welcome to my Multistep Form API Service",
        "database_status": connection_status,
    }


@app.post("/form", tags=["Subscription form"])
async def form():
    return {"msg": "subscription form"}
