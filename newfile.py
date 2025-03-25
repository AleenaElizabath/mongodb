import pymongo
dbcon=pymongo.MongoClient("mongodb://localhost:27017/")
db=dbcon["Aleena"]
col=db["Student"]
dict1={"_id":6,"Name":"aBc","Age":13,"Grade":"A"}
col.insert_one(dict1)
var1=col.find({},{"Grade":1})
for i in var1:
    print(i)