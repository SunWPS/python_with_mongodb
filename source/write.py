import pymongo

# connect to Mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password='example')

# select database
db = myclient["test"]

# select collection
col = db["mycollection"]

# insert single document
def insert_single():
    
    doc = {"Customer_id": "T55661122", "Country": "TH"}
    
    # write to collection
    x = col.insert_one(doc)
    
    print(x.inserted_id)


# insert multiple documents at once
def insert_multiple():
    
    mylist = []
    
    mylist.append({"Customer_id": "K88994455", "Country": "KR"})
    mylist.append({"Customer_id": "J77554466", "Country": "JP"})
    
    x = col.insert_many(mylist)
    
    print(x.inserted_ids)
    
insert_single()       
# insert_multiple()