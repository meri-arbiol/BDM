import json
import glob
from connection_mongo import connection_create, drop_collection
import pandas as pd


def loader_lookup_tables():
    print('INGESTING LOOKUP_TABLES FILES')
    db, server = connection_create()
    collection = 'lookup_tables'
    drop_collection(collection) #we remove the collection already created previously (in case it exists) to avoid ingest duplicate data
    list_files = glob.glob('data/lookup_tables/*')
    collection_currency = db[collection]
    for file in list_files:
        data = pd.read_csv(file)
        try:
            payload = json.loads(data.to_json(orient='records'))
            collection_currency.insert_many(payload)
        except:
            print(file + ' is empty')
    server.stop()
