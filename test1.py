# Extraction of data

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

password = "Rameswararao@1"
encoded_password = quote_plus(password)

uri = f"mongodb+srv://aravindsimha:{encoded_password}@datascience.kakeuwt.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["software_solutions"]
coll = db["information"]

# to get only comapny name in that

data = coll.find({"companyName": "google"})

for i in data:
    # print(i)
    # print(i) will print all the data so use
    print(i['companyName'])