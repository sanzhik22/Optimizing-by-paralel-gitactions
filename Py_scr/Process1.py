import csv

file = open('../Archive/Input1/overseas-trade.csv','r')
data = list(csv.reader(file, delimiter=","))
file.close()
print(data)

with open('../data/out1/output1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)