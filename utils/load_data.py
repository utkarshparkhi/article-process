from constant import db_config


def load_data():
    x = db_config.review_col.find(
        {"$and": [{"processed": False}, {"url": {"$exists": True}}, {"text": {"$exists": True}}]})
    return list(x)


import json


def load_data1():
    f = open("reviews.json", 'r')

    data = []
    while True:
        a = f.readline()
        if not a:
            break
        data.append(json.loads(a))
    return data
