import csv
import math
import numpy as np

def vote_func(mylist, myarray, k):
    
    ## print unknown's group candidate
    vote_result = []
    idx_num = 0
    while 1:
        if k <= idx_num:
            break
        vote_result.append(result_feature[mylist[idx_num]][0] )
        idx_num += 1
    print(vote_result)

    ## return best unknwon's group
    prediction = [0,0,0,0,0]
    idx_num = 0
    while 1:
        if k <= idx_num:
            break
        prediction[int(vote_result[idx_num])] += 1
        idx_num += 1
    return prediction.index(max(prediction))

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

## struct dataset
first_feature = np.zeros( [len(temp_data)-1, 1] )
second_feature = np.zeros( [len(temp_data)-1, 1] )
result_feature = np.zeros( [len(temp_data)-1, 1] )

first_unknown = np.zeros( [len(temp_data)-1, 1] )
second_unknown = np.zeros( [len(temp_data)-1, 1] )
distance = []

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
    elif compo_counter == 1 :
        second_feature[line_counter][0] = data[line_counter][compo_counter]
        compo_counter += 1
    else :
        result_feature[line_counter][0] = data[line_counter][compo_counter]
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

## calculate distances
line_counter = 0
while 1:
    if len(first_unknown) <= line_counter:
        break
    distance.append(math.sqrt( math.pow(first_feature[line_counter][0]-first_unknown[line_counter][0], 2) + 
                                            math.pow(second_feature[line_counter][0]-second_unknown[line_counter][0], 2) ) )
    line_counter += 1

## sort distance's index n predict unknown's group
idx = sorted(range(len(distance)), key=lambda k: distance[k])
group = vote_func(idx, result_feature, 11)
print(group)