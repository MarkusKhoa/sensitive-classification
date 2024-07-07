import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def init_mongo_collection():
    mongo_pass = os.getenv("MONGODB_PASSWORD")
    cluster = MongoClient(f"mongodb+srv://khoapham:{mongo_pass}@feedbacks.sommds7.mongodb.net/?retryWrites=true&w=majority&appName=feedbacks",
                          tls=True,
                          tlsAllowInvalidCertificates=True,
                          serverSelectionTimeoutMS=5000)
    db = cluster['ChatbotData']
    collection = db['sensitive_feedbacks']
    return collection

# feedback_data = {
#                 "text": "How many people are there",
#                 "prediction": "sensitive",
#                 "feedback": "Yes"
#             }
# collection = init_mongo_collection()
# collection.insert_one(feedback_data)

# print(f"Insert sample data successfully")   
