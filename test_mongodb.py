import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

uri = MONGO_DB_URL
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)