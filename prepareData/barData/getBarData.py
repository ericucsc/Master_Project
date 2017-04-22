#get bar data

import os
import csv
import json


outputJson = {}
for filename in os.listdir("./PermComByStates/"):
    with open('./PermComByStates/' + filename, 'rb') as csvfile:
        stateComData = list(csv.reader(csvfile))
        stateAbbr = filename[:-4]
        outputJson[stateAbbr] = []
        for eachRow in stateComData[1:]:
            outputJson[stateAbbr].append({"company" : eachRow[0].encode("utf8"), "workerCount" : eachRow[1]})

# print outputJson
#
with open('barData.json', 'w') as f:
    json.dump(outputJson, f)

# json.dump({"ca" : [{"com" : "netflix", "app" : "123"}, {"com" : "google", "app" : "2515"}], "tx" : 2}, f)
