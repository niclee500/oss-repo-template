from pymongo import MongoClient
client = MongoClient()
db = client.mongo_db_lab
collection = db.definitions
from bson.objectid import ObjectId
import random
import datetime

def random_word_requester():

    def_list = []
    for definition in collection.find():
        def_list.append(definition)
    random_def = random.choice(def_list)
    collection.update_one({"_id": random_def["_id"]}, {"$push": {"dates": str(datetime.datetime.isoformat(datetime.datetime.utcnow()))}})
    return collection.find({"_id": random_def["_id"]})


if __name__ == '__main__':
    print(random_word_requester())
