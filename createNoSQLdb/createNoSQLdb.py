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
    result = tmp.insert_many(data_to_add_list)

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

# Read the datasets to be added to the database
dtehvs1=''
dtehvs2=''
ivalve1=''
ivalve2=''

dtehvs1_data=load_json_file(dtehvs1)
dtehvs2_data=load_json_file(dtehvs2)
iValve1_data=load_json_file(ivalve1)
iValve2_data=load_json_file(ivalve2)

data_to_insert=[dtehvs1_data,dtehvs2_data,iValve1_data,iValve2_data]

connection=create_connection_with_client('BiomaterialTest')
add_one_data_set(connection,'heartvalve',dtehvs1_data)
add_one_data_set(connection,'heartvalve',dtehvs2_data)
add_one_data_set(connection,'heartvalve',iValve1_data)
add_one_data_set(connection,'heartvalve',iValve2_data)

# TopoChip screens
alp_bma_file=''
icam1_bma_file=''
topowellplate_file=''
phenome28_file=''
nanochip_file=''
mechano_transduction_file=''
dynamic_adaptation_file=''
monocytes_file=''

alp_data=load_json_file(alp_bma_file)
icam1_data=load_json_file(icam1_bma_file)
topowell_data=load_json_file(topowellplate_file)
phenome28_data=load_json_file(phenome28_file)
nanochip_data=load_json_file(nanochip_file)
mechano_transduction_data=load_json_file(mechano_transduction_file)
dynamic_adaptation_data=load_json_file(dynamic_adaptation_file)
monocytes_data=load_json_file(monocytes_file)

add_one_data_set(connection,'topochip',alp_data)
add_one_data_set(connection,'topochip',icam1_data)
add_one_data_set(connection,'topochip',topowell_data)
add_one_data_set(connection,'topochip',phenome28_data)
add_one_data_set(connection,'topochip',nanochip_data)
add_one_data_set(connection,'topochip',mechano_transduction_data)
add_one_data_set(connection,'topochip',dynamic_adaptation_data)
add_one_data_set(connection,'topochip',monocytes_data)
