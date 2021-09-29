import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017", username="root", password="example")

db = client['test']
col = db['mycollection']


# insert multiple documents with sub documents
def insert_multiple():
    
    mylist = []
    
    mylist.append({ "Cusomter_id": "T55997711", "Country": "TH", "simple_order_items": {"StockCode": "123456", "UnitPrice": 200, "Description":"pen" ,"Quantity": 40} })
    mylist.append({ "Cusomter_id": "T88997744", "Country": "TH", "simple_order_items": {"StockCode": "789101", "UnitPrice": 500, "Description": "apple" ,"Quantity": 10} })
    
    x = col.insert_many(mylist)
    
    print(x.inserted_ids)
    
    
def query_sub_document():
    
    query = {"simple_order_items.StockCode": "123456"}
    doc = col.find(query)
    
    for x in doc:
        print(x)
        

def update_sub_document():
    query = {"simple_order_items.StockCode": "123456"}
    newValues = {"$set": {"simple_order_items.StockCode": "654321"}}
    
    x = col.update_one(query, newValues)
    
    for x in col.find():
        print(x)

# insert_multiple()
# query_sub_document()
update_sub_document()