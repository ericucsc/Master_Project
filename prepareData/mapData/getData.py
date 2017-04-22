# This script is to get clean data for Viz for Master Project of Yanzhong Li

import csv

with open('./_PERM_StateByCase.csv', 'rb') as csvfile:
    permData = list(csv.reader(csvfile))

with open('./national_county.csv', 'rb') as csvfile:
    natNumData = list(csv.reader(csvfile))

permData[0] = ["stateAbbr", "applicantsCount", "stateName", "stateCode"]

for permRow in permData[1:]:
    for natRow in natNumData:
        if permRow[0] == natRow[0]:
            permRow.append(natRow[1])
            break

# # print permData
# with open('./permMap.csv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerows(permData)

tmpArray = ["05", "06", "17", "20", "28", "39", "48", "01", "19", "22", "27", "29", "31", "04", "08", "18", "26", "30", "36", "41", "51", "56", "37", "40", "47", "55", "02", "50", "38", "13", "23", "44", "54", "16", "46", "35", "53", "42", "12", "49", "21", "33", "45", "32", "15", "34", "09", "24", "25", "10", "11"]
with open('./temp.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(tmpArray)
