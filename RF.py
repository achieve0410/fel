import csv

## Empty array for save dataset
data = []

## open csv file and save dataset
f = open('cluster_origin_2.csv', 'r', encoding='utf-8')
csvReader = csv.reader(f)

for row in csvReader:
    data.append(row)

f.close()