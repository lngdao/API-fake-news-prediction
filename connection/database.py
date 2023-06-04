import certifi
from pymongo import MongoClient
from config import settings

ca_cert = certifi.where()

client = MongoClient(settings.mongo_uri, tlsCAFile=ca_cert)
db = client["fake_news"]
