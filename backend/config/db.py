from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
conn = MongoClient()

mongodb_url = 'mongodb+srv://favxlaw:Faveeee$@cluster0.8i0cb7i.mongodb.net/'
client = AsyncIOMotorClient(mongodb_url)
database = client.users
user_collection = database.get_collection('user_collection')


