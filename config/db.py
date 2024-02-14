from pymongo import MongoClient

conn = MongoClient(
    "mongodb+srv://oustin:jetNDM7rUjnRhL1F@cluster0.zxsnswl.mongodb.net/?retryWrites=true&w=majority")
db = conn.testing
collection = db.banpay
