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

db = client['software_solutions']
coll = db["information"]

list_of_records = [
    {'companyName': 'google',
     'product': 'AI model',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'google',
     'product': 'AI model',
     'courseOffered': 'Deep Learning for NLP and Computer Vision'},

    {'companyName': 'google',
     'product': 'AI model',
     'courseOffered': 'Data Science Master Program'},
]

# Check if the data already exists in the collection
existing_records = coll.find()
if len(list(existing_records)) == 0:
    # Insert the records only if they don't exist
    coll.insert_many(list_of_records)

# Rest of your code...
data1 = {"packetType":"D","data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":0,"batteryVoltageStable":"0","batteryVoltageOff":"12.42","batteryCrankParamTN":"-0.08","batteryCrankParamVN":"0.00","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"0.00","batteryCrankParamTT":"-0.00008","batteryCrankParamV0":"0.00","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36","batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99","vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00","coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":0,"imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[345345],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]},"header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":0,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification","pomVer":"1.0","headerVer":"V6","timestamp":0,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416","deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"}}


coll = db["added_information"]
# Check if the data already exists in the collection
existing_record = coll.find_one()
if not existing_record:
    # Insert the record only if it doesn't exist
    coll.insert_one(data1)

# Print the records
record = coll.find()
for i in record:
    print(i)
