from db.models.mongo import db
from bson.objectid import ObjectId


class Jobs:
    @classmethod
    def update_instance(cls, _name, _collection: str, _id: str, _dict: dict):
        collection = db[_collection]
        # TODO: Custom Exception
        if id is None:
            raise Exception("Exception Found")

        instance = collection.find_one({'_id': ObjectId(_id)})

        if instance is None:
            raise Exception('Record not found')

        collection.update_one({'_id': ObjectId(_id)}, {'$set': _dict})
        # TODO: Console styling
        print('Running job ' + _name)


