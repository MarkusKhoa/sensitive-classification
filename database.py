import os
import certifi

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def init_mongo_collection():
    mongo_pass = os.getenv("MONGODB_PASSWORD")
    cluster = MongoClient(f"mongodb+srv://khoapham:{mongo_pass}@feedbacks.sommds7.mongodb.net/?retryWrites=true&w=majority&appName=feedbacks&tlsCAFile=isrgrootx1.pem",
                          tls=True,
                          tlsAllowInvalidCertificates=True, 
                          serverSelectionTimeoutMS=5000,
                          ca = certifi.where())
    db = cluster['ChatbotData']
    collection = db['sensitive_feedbacks']
    return collection
