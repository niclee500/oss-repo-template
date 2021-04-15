from pymongo import MongoClient
client = MongoClient()
from bson.objectid import ObjectId

if __name__ == '__main__':
    db = client.mongo_db_lab

    # All records
    for definition in db.definitions.find():
        print(definition)

    # One record
    print(db.definitions.find_one())

    # Specific records
    specific_word = db.definitions.find({"word": "Zoomie"})
    print(specific_word)

    # By object # ID
    print(db.definitions.find({'_id': ObjectId('56fe9e22bad6b23cde07b8b7')}))

    # Inserting a new word
    new_word = {"word": "Bathroom",  "definition": "sad place to be"}
    db.definitions.insert_one(new_word)
    print(db.definitions.find_one({"word": "Bathroom"}))
