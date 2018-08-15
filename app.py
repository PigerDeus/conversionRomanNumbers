from flask import Flask
from config import Configuration
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Configuration)
client = MongoClient('mongodb', 27017)
db = client.numb_db



