import csv
import json
from collections import OrderedDict
import math
import numpy as np

## Empty list for save dataset
header = []
temp_data = []

## variable for count # of lines
line_counter = 0

## read data from csv file
with open('driving_score_180ea.csv') as f:
    while 1:
        data = f.readline().replace("\n","")

        if not data: break
        if line_counter == 0:
            header = data.split(",")
        else:
            temp_data.append(data.split(","))
        line_counter = line_counter + 1

## Variable for making json file
file_data = OrderedDict()
line_counter = 0

## construct json file
while 1:
    data = temp_data
    if (line_counter>=len(temp_data)):
        break
    else:
        file_data["%d" % line_counter] = { 'compliance': '%d' % int(temp_data[line_counter][0]),
                                        'acceleration': '%d' % int(temp_data[line_counter][1]),
                                        'deceleration': '%d' % int(temp_data[line_counter][2]),
                                        'result': '%d' % int(temp_data[line_counter][3])}
    
        line_counter = line_counter + 1    

file_data["number"] = line_counter

## print json file
print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

## save json file
with open('words.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


#file_data["name"] = "COMPUTER"
#file_data["language"] = "kor"
#file_data["words"] = {'ram':'RAM', 'process':'PROCESS', 'processor':'PROCESSOR', 'cpu':'CPU'}
#file_data["number"] = 4

