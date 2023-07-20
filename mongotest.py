import pymongo
# import urllib
client = pymongo.MongoClient("mongodb+srv://kumaka6:Mani%40143K@clustermangodb.ssexieu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"kumaka",
    "email":"kumaka6@gmail.com",
    "surname": "vengadajalam"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

"""
HELP on password must be escaped error: 
https://stackoverflow.com/questions/39237813/how-to-escape-in-a-password-in-pymongo-connection

Whenever you have '@' in your MongoDB password and would want to connect with your URI, simply replace it using %40
check other answers also. 

Note:2

had ERROR :: OperationFailure: Unsupported OP_QUERY command: insert. The client driver may require an upgrade

updated the driver as per link  
$ python -m pip install --upgrade pymongo
https://www.mongodb.com/docs/drivers/pymongo/
"""
# updated