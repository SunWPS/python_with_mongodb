import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="example")

db = client['test']
col = db['mycollection']


# add attributes to the document
def add_attributes_to_document():
    
    query = {"Customer_id": "T55661122"}
    newvalues = {"$set": {"Name": "Wongsakorn"}}
    
    x = col.update_one(query, newvalues)
    
    for x in col.find(query):
        print(x)


# change attributes of the document
def update_document():
    query = {"Customer_id": "T55661122"}
    newvalues = {"$set": {"Name": "Wongsakorn Pinvasee"}}
    
    x = col.update_one(query, newvalues)
    
    for x in col.find(query):
        print(x)
        
add_attributes_to_document()
# update_document()