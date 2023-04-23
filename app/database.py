import pymongo
from pymongo import mongo_client

from app.config import Settings

settings = Settings()
client = mongo_client.MongoClient(settings.MONGODB_DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE] #store_db

ItemCol = db.item
ItemCol.create_index([("name", pymongo.ASCENDING)], unique=True)