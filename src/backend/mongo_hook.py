import pymongo
import login_config as cf 

def create_DB(db_name: str):
    myclient = pymongo.MongoClient(cf.host)
    dblist = myclient.list_database_names()

    if (db_name in dblist):
        print("Database exists!")
    else:
        mydb = myclient.get_database(db_name)
        print("Database created!")

def create_collection(db_name: str, collection_name: str):
    myclient = pymongo.MongoClient(cf.host)

    mydb = myclient[db_name]
    collist = mydb.list_collection_names()

    if (collection_name in collist):   
        print("Collection exists!")
    else:
        mycol = mydb.get_collection(collection_name)
        print("Collection created!")

def insert_one_DB(db_name: str, collection_name: str, document: dict):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    x = mycol.insert_one(document)

    print("Insert ID: ", x.inserted_id)

def insert_many_DB(db_name: str, collection_name: str, document: list[dict]):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    x = mycol.insert_many(document)
    print("Insert ID list: ", x.inserted_id)

def find_one_document(db_name: str, collection_name: str):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    mydoc = mycol.find_one()

    return mydoc

def find_all_document(db_name: str, collection_name: str, lim: int = 0):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    if (lim):
        mydoc = mycol.find().limit(lim)
    else:
        mydoc = mycol.find()

    return mydoc

def find_selected_document(db_name: str, collection_name: str, selected_fields: dict):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    mydoc = mycol.find({}, selected_fields)

    return mydoc

def query_document(db_name: str, collection_name: str, query: dict):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)
    queryList = list()

    myquery = mycol.find(query)

    for item in myquery:
        queryList.append(item)

    return queryList

def sort(db_name: str, collection_name: str, field: str, order: int = 1):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    mydocSorted = mycol.find().sort(field, order)

    return mydocSorted

def delete_one_doc(db_name: str, collection_name: str, query: dict):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    mycol.delete_one(query)
    print(x.deleted_count, " documents deleted.")   

def delete_many_doc(db_name: str, collection_name: str, query: dict):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    mycol.delete_many(query)  
    print(x.deleted_count, " documents deleted.")

def delete_all(db_name: str, collection_name: str):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    mycol.delete_many({})  
    print(x.deleted_count, " documents deleted.")

def drop_collection(db_name: str, collection_name: str):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    mycol.drop()
    print("Collection ", collection_name, " is dropped")

def update_one_doc(db_name: str, collection_name: str, query: dict, newVal: dict):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    newvalues = { "$set": newVal }

    x = mycol.update_one(query, newvalues)
    print(x.modified_count, "documents updated.")

def update_many_doc(db_name: str, collection_name: str, query: dict, newVal: dict):
    myclient = pymongo.MongoClient(cf.host)
    mydb = myclient.get_database(db_name)
    mycol = mydb.get_collection(collection_name)

    newvalues = { "$set": newVal }

    x = mycol.update_many(query, newvalues)
    print(x.modified_count, "documents updated.")
