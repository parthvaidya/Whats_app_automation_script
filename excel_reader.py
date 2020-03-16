from csv import reader
l =[]
with open('sample.csv',"r") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        l.append(row[0])

print(l)