from sshtunnel import SSHTunnelForwarder
import pymongo


def connection_create():
    MONGO_HOST = "10.4.41.47"
    MONGO_DB = "bdm_p1"
    MONGO_USER = "bdm"
    MONGO_PASS = "bdm"

    server = SSHTunnelForwarder(
        MONGO_HOST,
        ssh_username=MONGO_USER,
        ssh_password=MONGO_PASS,
        remote_bind_address=('127.0.0.1', 27017)
    )

    server.start()

    client = pymongo.MongoClient('127.0.0.1', server.local_bind_port) # server.local_bind_port is assigned local port
    db = client[MONGO_DB]
    return db, server


def drop_collection(collection):
    db, server = connection_create()
    mycol = db[collection]
    mycol.drop()
