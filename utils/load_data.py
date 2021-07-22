from constant import db_config


def load_data():
    x = db_config.review_col.find(
        {"$and": [{"processed": False}, {"url": {"$exists": True}}, {"text": {"$exists": True}}]})
    return list(x)


import json


def load_data1():
    f = open("/content/drive/MyDrive/reviews.json", 'r')
    overall_ct = 0
    data = []
    count = 0
    b = False
    while True:
        a = f.readline()
        if not a:
            break
        if b:
            data.append(json.loads(a))

        count += 1
        overall_ct += 1
        if count == 1060:
            b = True
            count = 0
        if (count == 30 and b):
            print(overall_ct)
            count = 0
            yield data
            data = []
    yield data
