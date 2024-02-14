import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv('.env')

user_name = os.getenv('MONGO_USER_NAME')
password = os.getenv('MONGO_PASSWORD')

conn = MongoClient(
    f'mongodb+srv://{user_name}:{password}@cluster0.zxsnswl.mongodb.net/?retryWrites=true&w=majority')
db = conn.testing
collection = db.banpay
