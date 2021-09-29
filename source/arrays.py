import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="example")

db = client["test"]
col = db["mycollection"]


# insert multiple documents with sub documents 
def insert_array():

    query = {"Cusomter_id": "T55887799", "complex_order_items": [{"StockCode" : "124578", "UnitPrice":2000, "Description":"chair" ,"Quantity" : 2},\
        {"StockCode" : "789456", "UnitPrice":455, "Description":"book" ,"Quantity" : 5} ]}
    
    x = col.insert_one(query)
    
    print(x.inserted_id)

    
def query_by_subdocuments():
    
    query = {"complex_order_items.StockCode": "789456"}
    doc = col.find(query)
    
    for x in doc:
        print(x)
        

def add_subdocument_to_array():
    query = {"Cusomter_id": "T55887799"}
    newcar = {"$push": {"complex_order_items": {"StockCode" : "879562", "UnitPrice":2000000, "Description":"4x4" ,"Quantity" : 1}}}
    
    x = col.update_one(query, newcar)
    
    print(x.matched_count, "updated")
    
    for x in col.find(query):
        print(x)
        
# insert_array()
# query_by_subdocuments()
add_subdocument_to_array()