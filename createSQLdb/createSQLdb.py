import sqlite3
from sqlite3 import Error
import pandas as pd

# Create the connection

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to SQLite DB is established')
    except Error as e:
        print(f"The error '{e}'occured")

    return connection

# Create a table
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def write_pandas_dataframe_to_db(connection,pd_df,table_name):
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT * FROM '''+table_name)
        if cursor.fetchone().__len__()!=0:
            # table exists
            print('table exists')
        else:
            # add the table
            pd_df.to_sql(table_name,connection,if_exists='append',index=False)
            print('Table with name %s added' % table_name)
    except Error as e:
        print(f"The error '{e}' occurred")
        
 def read_txt_files(path_to_file,separator):
    return pd.read_csv(file=path_to_file,sep=separator)

def transform_df_to_dict(dataframe):
    return dataframe.to_dict()

def load_json_file(path_to_json):
    with open(path_to_json) as f:
        data=json.load(f)
    return data
