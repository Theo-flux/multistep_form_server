from motor.motor_asyncio import AsyncIOMotorClient

from settings import mongodb_uri, port


client = AsyncIOMotorClient(mongodb_uri, port)


def ping_database():
    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return "connected to database!"
    except Exception as e:
        print(e)
        return "unable to connect to database!"


def get_database():
    # get database from cluster
    res = ping_database()
    if res:
        return client["form"]
