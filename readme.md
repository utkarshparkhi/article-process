#Article Process
###Setting Up
1. add db config in file `constant/db_config.py`
   ```python
    client = pymongo.MongoClient("DB_PATH")
    review_db = client["REVIEW_DB_NAME"]
    review_col = review_db["REVIEW_COLLECTION_NAME"]
    
    processed_db = client["PROCESSED_DATA_DB_NAME"]
    processed_col = processed_db["PROCESSED_DATA_COLLECTION_NAME"]

    ```
   
2) run `./main.py`<br>
   `python ./main.py`