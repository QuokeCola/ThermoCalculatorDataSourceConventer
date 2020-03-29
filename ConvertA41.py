import csv
cool = csv.reader(open("TableA41.csv",'r'))
newRecords=[]
for record in cool:
    newRecord = record[0].split(" ")
    newRecords.append(newRecord)
output = open('output41.csv', 'w')
outputstr = []
for record in newRecords:
    outputstr.append(",".join(record)+"\n")
output.writelines(outputstr)