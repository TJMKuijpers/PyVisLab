from pymongo import MongoClient
import pandas as pd
import json

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

def add_multiple_files(database,identifier,data_to_add_list):
    tmp = database[identifier]
    result = tmp.inser_many(data_to_add_list)

def delete_record_from_database(connection,identifier,query):
    tmp=connection[identifier]
    result = tmp.delete_one(query)

def read_txt_files(path_to_file,separator):
    return pd.read_csv(file=path_to_file,sep=separator)

def transform_df_to_dict(dataframe):
    return dataframe.to_dict()

def load_json_file(path_to_json):
    with open(path_to_json) as f:
        data=json.load(f)
    return data
