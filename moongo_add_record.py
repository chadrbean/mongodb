import pymongo
import json
import sys
import time

start_time = time.time()
connection = pymongo.MongoClient("mongodb://localhost")
db=connection.chad_test
collection = db.newtest
source_name = sys.argv[2].strip()
count = 1
with open(sys.argv[1], "r") as line:
    dic_add = []
    for record in line:
        if count % 500000 == 0:
            collection.insert_many(dic_add)
            dic_add = []
            count = 1
        j = json.loads(record)
        if "emails" not in j:
            continue
        j["source"] = source_name
        for e in j["emails"]:
            try:
                j.pop("emails")
                j["email"] = e["address"]
                dic_add.append(j)
                count += 1
            except:
                continue

sectime = (time.time() - start_time)
print(f'Length Of Run{sectime}')
print(f'Average Read Speed {(count/(sectime/60))} per minute')
