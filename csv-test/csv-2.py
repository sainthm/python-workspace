import csv

f = open('csv_sample2.csv', 'r')
rdr = csv.reader(f)

for line in rdr:
    print(line)

f. close()