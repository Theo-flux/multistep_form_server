from os import environ
from dotenv import load_dotenv


load_dotenv()

# MongoDB attributes
MONGO_USER = environ.get("FASTAPI_MONGO_USER")
MONGO_PASSWORD = environ.get("FASTAPI_MONGO_PASSWORD")
mongodb_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@form.gd9jpea.mongodb.net/?retryWrites=true&w=majority"
port = 8000
