from pymongo import MongoClient
import os

MONGO_URI = "mongodb+srv://adibmuzammilali_db_user:7NkYs5xl7os7zFPV@cluster0.s8zrt8j.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["smart_internship_db"]

users_collection = db["users"]
reports_collection = db["reports"]
passports_collection = db["passports"]

def get_db():
    return db