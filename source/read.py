import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017", username="root", password="example")
db = client['test']
col = db['mycollection']

query = {"Customer_id": "T55661122"}
doc = col.find(query)

# return only Customer_id
returnOnly = {"_id": 0, "Customer_id": 1}
doc = col.find(query, returnOnly)

for x in doc:
    print(x)
    
    
# sort the data
# ASC .sort("Customer_id") | .sort("Customer_id", 1)
# DESC .sort("Customer_id", -1)