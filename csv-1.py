#-*- coding:utf-8 -*-
import csv

with open('./sample1.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.reader(f)

    print(reader)
    print(type(reader))
    print(dir(reader))

    for txt in reader:
        print(txt)