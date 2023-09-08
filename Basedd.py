from pymongo import MongoClient
import certifi
from dotenv import load_dotenv
import os
load_dotenv()
user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')
hostname = os.getenv('MONGO_HOSTNAME')

MONGO_URI = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["Productos"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db