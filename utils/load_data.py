from constant import db_config


def load_data():
    x = db_config.review_col.find(
        {"$and": [{"processed": False}, {"url": {"$exists": True}}, {"text": {"$exists": True}}]})
    return list(x)
