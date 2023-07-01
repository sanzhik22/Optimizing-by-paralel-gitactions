import csv

file = open('../Archive/Input2/table2.csv','r')
data = list(csv.reader(file, delimiter=","))
file.close()
print(data)

with open('../data/out2/output2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)