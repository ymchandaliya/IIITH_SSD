import csv

dataFile = open("lab_11_data.csv")

data = []

l = csv.reader(dataFile,delimiter = ",")

for x in l:
    if(x[-7] != '% Chng'):
        data.append(x[0:-6])


rArray = list(filter(lambda x: (float(x[-1])>-3.0), data))
s = 0
y = 0

oList = [[float(rArray[i][1].replace(",","")) for i in range(len(rArray))]]
hList = [[float(rArray[i][2].replace(",","")) for i in range(len(rArray))]]
lList = [[float(rArray[i][3].replace(",","")) for i in range(len(rArray))]]

oAvg = list(map(lambda x: sum(x)/len(x), oList))
hAvg = list(map(lambda x: sum(x)/len(x), hList))
lAvg = list(map(lambda x: sum(x)/len(x), lList))


opFile = open("avg_output.txt", "w")
opFile.write("open " + str(oAvg[0]) + "\n")
opFile.write("low" + str(lAvg[0]) + "\n")
opFile.write("high" + str(hAvg[0]) + "\n")
opFile.close()

c = input("Enter character to match: ")
dataOP = []
for i in rArray:
    if(i[0][0] == c):
        print(i)
        dataOP.append(i)

opFile1 = open("stock_output.txt", "w")

for z in dataOP:
    stToWrite = ""
    for _ in z:
        stToWrite += str(_) + " "
    stToWrite += "\n"
    opFile1.write(stToWrite)

opFile1.close()

