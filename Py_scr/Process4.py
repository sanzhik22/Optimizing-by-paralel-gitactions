import csv

file = open('Archive/Input4/table4.csv','r')
data = list(csv.reader(file, delimiter=","))
file.close()
print(data)

with open('data/out4/out_table_seq2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)