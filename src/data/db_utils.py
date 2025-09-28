import pymongo
from sqlalchemy import create_engine
import pandas as pd
 
def get_mongo_collection(uri,db_name,collection):
    client=pymongo.MongoClient(uri)
    return client[db_name][collection]

def get_sql_engine(user,password,host,port,database):
    uri=f"postgresql://{user}:{password}@{host}:{port}/{database}" 
    return create_engine(uri)

def mongo_to_sql(mongo_coll,sql_engine,sql_table):
    df=pd.DataFrame(list(mongo_coll.find()))
    df.to_sql(sql_table,sql_engine,if_exists="replace",index=False)
    print(f"Loaded{len(df)}rows to  SQL table{sql_table}")