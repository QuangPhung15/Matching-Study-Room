import pymongo
import mongo_hook as mgh 
import login_config as cf 

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# dblist = myclient.list_database_names()
# print(dblist)

data = {"user_name": "admin", "password": "admin"}
# newData = {"a": "d"}

mgh.insert_one_DB(cf.database, cf.loginCollection, data)
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# dblist = myclient.list_database_names()
# print(dblist)

# mgh.update_one_doc(cf.database, cf.loginCollection, data, newData)

# query = mgh.query_document(cf.database, cf.loginCollection, newData)
# print(query)
# for item in query:
#     print(item['a'])