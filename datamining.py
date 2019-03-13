import csv
import math
import numpy as np

## Empty list for save dataset
header = []
temp_data = []

## variable for count # of lines
line_counter = 0

## read data from csv file
with open('test_data.csv') as f:
    while 1:
        data = f.readline().replace("\n","")
        # print(data)
        if not data: break
        if line_counter == 0:
            header = data.split(",") # 
        else:
            temp_data.append(data.split(","))
        line_counter = line_counter + 1

## set train & test data
first_feature = np.zeros( [len(temp_data)-1, 1] )
second_feature = np.zeros( [len(temp_data)-1, 1] )

first_unknown = np.zeros( [len(temp_data)-1, 1] )
second_unknown = np.zeros( [len(temp_data)-1, 1] )

## variables for array
line_counter = 0
compo_counter = 0

## divide feature
while 1:
    data = temp_data
    if len(data)-1 <= line_counter:   
        first_unknown[0][0] = data[line_counter][compo_counter]
        compo_counter += 1
        second_unknown[0][0] = data[line_counter][compo_counter]
        break

    if compo_counter == 0 :
        first_feature[line_counter][0] = data[line_counter][compo_counter]
        compo_counter += 1
    else :
        second_feature[line_counter][0] = data[line_counter][compo_counter]
        line_counter += 1
        compo_counter = 0

## copy
line_counter = 1
while 1:
    if len(first_unknown) <= line_counter:
        break

    first_unknown[line_counter][0] = first_unknown[0][0]
    second_unknown[line_counter][0] = second_unknown[0][0]
    line_counter += 1


# list1 = [[1,2],[3,4]]
# list2 = [[3,4],[1,2]]
# a=np.array(list1)
# b=np.array(list2)

# c=np.dot(a,b)
# print(c)