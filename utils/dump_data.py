from constant import db_config
import json
from bson import json_util


def dump_data(data):
    x = []
    for d in data:
        x.append(insert(d))

    db_config.review_col.update_many({"_id": {"$in": x}}, {"$set": {"processed": True}})
    db_config.processed_col.update_many({"_id": {"$in": x}}, {"$set": {"processed": True}})
    return x


def insert(data):
    if db_config.processed_col.find_one({"_id": data['_id']}) is not None:
        x = db_config.processed_col.update_one({"_id": data["_id"]}, {"$set": data})
        return data["_id"]
    else:
        x = db_config.processed_col.insert_one(data)
        return x.inserted_id


def dump_data1(data):
    f = open("/content/drive/MyDrive/review_out.json", "a")
    for d in data:
        json.dump(d, f, default=json_util.default)
        f.write('\n')
    return True
