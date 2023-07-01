from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kkshetty:JWL3e4UC6GK4Swd@pwskills.sfce3qx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["flask_app_1"]
login_credentials = db["login_credentials"]
user_details = db["user_details"]

def check_user(email):
    # print(email) 
    return login_credentials.count_documents({'email': email}) == 1

def extract_pswd(email):
    cursor = login_credentials.find_one({'email': email})
    return cursor['password']

def extract_user_details(email):
    cursor = user_details.find_one({'email': email})
    first_name = cursor['first_name']
    last_name = cursor['last_name']
    state = cursor['state']
    city = cursor['city']
    return (first_name, last_name, state, city)

def insert_record(record, collection):
    db[collection].insert_one(record)

