import pymongo
import json
import sys
import time

start_time = time.time()
connection = pymongo.MongoClient("mongodb://localhost")
db=connection.chad_test
collection = db.fivemillargeload

count = int(0)
n = 100000
startrange = 0
stoprange = 100000
data = ["768327048e394ac3810dd7a6c0ac848f.protect@whoisguard.com", "wesley@scottcalvintech.com", "YuMing@YinSiBaoHu.AliYun.com"]
with open(sys.argv[1], "r") as f:
    for i in f:
        for record in range(startrange,stoprange):
            data.append(i.strip("\n"))
        result = collection.find({"emails":{"address":data}})
        for each in result:
            print(each)
            print("got here")
            input()
        data =[]
        
        startrange = stoprange
        stoprange = startrange + n
        

sectime = (time.time() - start_time)
print(f'Total Records Added {count}')
print(f'Length Of Run{sectime}')
print(f'Average Read Speed {(count/(sectime/60))} per minute')
