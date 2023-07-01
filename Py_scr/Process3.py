import csv

file = open('Archive/Input3/table3.csv','r')
data = list(csv.reader(file, delimiter=","))
file.close()
print(data)

with open('data/out3/output3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)