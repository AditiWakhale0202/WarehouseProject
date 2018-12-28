import pymongo
client = pymongo.MongoClient()
db = client.mydb
collection = db.warehouse
for post in collection.find():
    print "Product is "+post['product']+" of brand "+post['brand']