from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
conn = MongoClient()

mongodb_url = ' mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1'
client = AsyncIOMotorClient(mongodb_url)
database = client.users
user_collection = database.get_collection('user_collection')


