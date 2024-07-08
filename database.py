import os
import certifi
import streamlit as st

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def init_mongo_collection():
    mongo_pass = os.getenv("MONGODB_PASSWORD")
    ca = certifi.where()
    # uri = f"mongodb+srv://khoapham:{mongo_pass}@feedbacks.sommds7.mongodb.net/?retryWrites=true&w=majority&appName=feedbacks"
    uri = st.secrets.db_credentials.DB_URI
    cluster = MongoClient(uri, tls = True, tlsCAFile = ca, serverSelectionTimeoutMS = 5000)
    db = cluster['ChatbotData']
    collection = db['sensitive_feedbacks']
    return collection
