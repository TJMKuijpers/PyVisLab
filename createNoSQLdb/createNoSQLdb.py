from pymongo import MongoClient


def create_connection_with_client(database_name):
    client = MongoClient()
    try:
        database=client[database_name]
        return database
    except Exception as e:
        print(f"The error '{e}' occurred")

def add_one_data_set(database,identifier,data_to_add):
    tmp = database[identifier]
    result = tmp.insert_one(data_to_add)
