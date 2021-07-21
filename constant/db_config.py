import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
review_db = client["review_db"]
review_col = review_db["reviews"]

processed_db = client["process_db_test"]
processed_col = processed_db["processed_col"]
