import csv

file = open('data/out4/output10.csv','r')
data = list(csv.reader(file, delimiter=","))
file.close()
print(data)

with open('data/out5/output10.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)