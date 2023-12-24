from fastapi import FastAPI, Body

from database import ping_database, get_database
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


@app.get("/", tags=["Welcome"])
async def welcome():
    connection_status = ping_database()
    return {
        "message": "Welcome to my Multistep Form API Service",
        "database_status": connection_status,
    }


@app.post("/form", tags=["Subscription form"])
async def step_form_post(form_data: FormModel = Body(...)):
    db_name = get_database()
    print(db_name)
    return {"msg": "subscription form"}
