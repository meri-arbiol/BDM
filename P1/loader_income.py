import json
import glob
from connection_mongo import connection_create, drop_collection
import pandas as pd


def loader_income():
    print('INGESTING OPENDATABCN-INCOME FILES')
    db, server = connection_create()
    collection = 'opendatabcn_income'
    drop_collection(collection) #we remove the collection already created previously (in case it exists) to avoid ingest duplicate data
    list_files = glob.glob('data/opendatabcn-income/*')
    collection_currency = db[collection]
    for file in list_files:
        data = pd.read_csv(file)
        try:
            payload = json.loads(data.to_json(orient='records'))
            collection_currency.insert_many(payload)
        except:
            print(file + ' is empty')
    server.stop()
