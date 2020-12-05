import  json
x={
    "Name":"Chandler",
    "Age":25,
    "city":"",
    "grade": None,
    "result": True,
    "marks1":{"maths":95,"CS":100},
    "marks2":[70,58,99],
    "avg":98.99
}
y=json.dumps(x)
print(y)
print(json.dumps((1,2,3)))
print(json.dumps(list(range(9))))

from pymongo import MongoClient
myclient=MongoClient("mongodb://localhost:27017/") #making connection
db=myclient["XYZ"] #database
Collection=db["data"]
with open('D:\\P\intern-python\\task12\\data.json') as f:
    file_data=json.load(f)
if isinstance(file_data,list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)