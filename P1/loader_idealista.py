import json
import glob
from connection_mongo import connection_create, drop_collection


def loader_idealista():
    print('INGESTING IDEALISTA FILES')
    db, server = connection_create()
    collection = 'idealista'
    drop_collection(collection) #we remove the collection already created previously (in case it exists) to avoid ingest duplicate data
    list_files = glob.glob('data/idealista/*')
    collection_currency = db[collection]
    for file in list_files:
        parse_filename = file.split('/')[2].split('_')[0:3]
        with open(file) as f:
            file_data = json.load(f)
        for i in range(len(file_data)):
            date = {'date': parse_filename[0]+'-'+parse_filename[1]+'-'+parse_filename[2]}
            date.update(file_data[i])
            file_data[i] = date
        try:
            collection_currency.insert_many(file_data)
        except:
            print(file + ' is empty')
    server.stop()
