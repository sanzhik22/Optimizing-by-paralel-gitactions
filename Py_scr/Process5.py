import csv

file = open('Archive/Input5/table5.csv','r')
data = list(csv.reader(file, delimiter=","))
file.close()
print(data)

with open('data/out5/output5.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)