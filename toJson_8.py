import csv
import json
from collections import OrderedDict

## Empty list for save dataset
header = []
temp_data = []

## variable for count # of lines
line_counter = 0

## read data from csv file
with open('driving_score_train9.csv') as f:
    while 1:
        data = f.readline().replace("\n","")

        if not data: break
        if line_counter == 0:
            header = data.split(",")
        else:
            temp_data.append(data.split(","))
        line_counter += 1

## Variable for making json file
file_data = OrderedDict()
file_data["header"] = {}
file_data["data"] = {}

line_counter = 0

## construct json file
while 1:
    data = temp_data
    if (line_counter>=len(data)):
        break
    else:
        file_data["data"]["%d" % line_counter] = { 'distance': '%d' % int(data[line_counter][0]),
                                        'average speed': '%d' % int(data[line_counter][1]),
                                        'number of acceleration': '%d' % int(data[line_counter][2]),
                                        'number of sudden starts': '%d' % int(data[line_counter][3]),
                                        'number of abrupt lane changes': '%d' % int(data[line_counter][4]),
                                        'number of intense brakes': '%d' % int(data[line_counter][5]),
                                        'number of sudden stops': '%d' % int(data[line_counter][6]),
                                        'number of abrupt steerings': '%d' % int(data[line_counter][7]),
                                        'result': '%f' % float(data[line_counter][8]),}
    
        line_counter += 1  

file_data["header"]["number"] = line_counter

## print json file
print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

## save json file
with open('test2.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


