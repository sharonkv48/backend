# from pymongo import MongoClient

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# # Create a new client and connect to the server

# uri = "mongodb+srv://nemesis:byojRtJ1a9GWbvUU@cluster0.ixa4p.mongodb.net/backend_api?retryWrites=true&w=majority&appName=Cluster0"
# client = MongoClient(uri, server_api=ServerApi('1'))


# client = MongoClient(uri, server_api=ServerApi('1'))

# db = client['test']
# collection = db["test_collection"]
# mentor_collection = db["mentor_collection"]



from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
uri = "mongodb+srv://nemesis:byojRtJ1a9GWbvUU@cluster0.ixa4p.mongodb.net/backend_api?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['backend_api']
collection = db["test_collection"]
mentor_collection = db["mentor_collection"]
chat_collection = db["chats"]  # New collection for chat data