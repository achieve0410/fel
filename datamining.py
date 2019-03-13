import csv
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
        # print(data)
        if not data: break
        if line_counter == 0:
            header = data.split(",") # 
        else:
            temp_data.append(data.split(","))
        line_counter = line_counter + 1

# print(header)
# print(temp_data)

## set train & test data
first_feature = np.zeros( [len(temp_data), 1] )
second_feature = np.zeros( [len(temp_data), 1] )

## variables for array
line_counter = 0
compo_counter = 0

## temp_data to train/test data ( list (1 dim.) -> array (2 dim.) )
while 1:
    data = temp_data
    if len(data)<=line_counter: break

    if compo_counter == 0 :
        first_feature[line_counter][0] = data[line_counter][compo_counter]
        compo_counter += 1
    else :
        second_feature[line_counter][0] = data[line_counter][compo_counter]
        line_counter += 1
        compo_counter = 0

print(first_feature)
print(second_feature)

# list1 = [[1,2],[3,4]]
# list2 = [[3,4],[1,2]]
# a=np.array(list1)
# b=np.array(list2)

# c=np.dot(a,b)
# print(c)