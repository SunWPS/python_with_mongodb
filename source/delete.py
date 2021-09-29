import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="example")

db = client['test']
col = db['mycollection']

# delete single document
def delete():
    
    query = {'Customer_id': "T55661122"}
    
    # if there are multiple ones it only deletes one
    x = col.delete_one(query)
    
    print(x.deleted_count, "deleted")
    
delete()