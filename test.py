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


list_of_records = [
    { 'companyName' : 'google',
      'product' : 'AI model',
      'courseOffered' : 'Machine Learning with Deployment'},

    { 'companyName' : 'google',
      'product' : 'AI model',
      'courseOffered' : 'Deep Lerning for NLP and Computer visison'},

    { 'companyName' : 'google',
      'product' : 'AI model',
      'courseOffered' : 'Data Science Master Program'},

]

db = client['software_solutions']
coll = db["information"]
coll.insert_many(list_of_records)