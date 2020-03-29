import csv
cool = csv.reader(open("TableA32.csv",'r'))
newRecords=[]
for record in cool:
    newRecord = record[0].split(" ")
    secondtolast = record[1:-1]
    secondtolast.append(record[-1])
    for cell in secondtolast:
        if cell.__contains__(" "):
            splitcell = cell.split(" ")
            newRecord[-1] += splitcell[0]
            if(splitcell[1] != ''):
                newRecord.append(splitcell[1])
        else:
            if(cell != ''):
                newRecord.append(cell)
    for i in range(len(newRecord)-1):
        if newRecord[i]=='':
           del newRecord[i]
    newRecords.append(newRecord)
output = open('output32.csv', 'w')
outputstr = []
for record in newRecords:
    outputstr.append(",".join(record)+"\n")
output.writelines(outputstr)