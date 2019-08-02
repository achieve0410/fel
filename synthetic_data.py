import csv
import math
import random
from matplotlib import pyplot as plt
import numpy as np

## Empty list for save dataset
temp_data = []
syn_data = []

def load_csv(filepath):
    data = []
    line_count = 0
    with open(filepath, encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        for row in reader:
            if line_count == 0: 
                line_count += 1
                continue
            else: data.append(row)
    return data

def write_csv(filepath, data):
    csvfile = open(filepath, "w", newline="")

    csvwriter = csv.writer(csvfile)

    for rows in data:
        csvwriter.writerow(rows)
    
    csvfile.close()

def getResultNum(originData, data):

    minValue = 99999
    retNum = 0
    for row in originData:
        temp_sum = 0
        for i in range(len(row)-1):
            diff = pow((int(row[i]) - data[i]),2)
            temp_sum += diff
        
        if minValue >= temp_sum:
            minValue = temp_sum
            retNum = float(row[-1])
        
    return retNum

def generateSyntheticData(originData):
    data = []

    for i in range(len(originData[0])-1):
        if i >= 2:
            randomNum = random.randint(1, 10)
        else:
            randomNum = random.randint(0, 9)
        data.append(randomNum)
    
    randomNum = getResultNum(originData, data)
    data.append(randomNum)

    return data

def generateSyntheticData_2(originData):
    data = []

    for i in range(len(originData[0])-1):
        if i >= 2:
            randomNum = random.randint(0, 9)
        else:
            randomNum = random.randint(1, 10)
        data.append(randomNum)
    
    randomNum = getResultNum(originData, data)
    data.append(randomNum)

    return data

## load data from csv file
temp_data = load_csv("modified_data.csv")
# print(len(temp_data))




## generate random data
genNum = 200000
for i in range(genNum):
    mylist = generateSyntheticData_2(temp_data)
    syn_data.append(mylist)
    # temp_data.append(mylist)
# print(len(temp_data))
# print(temp_data)







## after visualization
####################################################################################################
x_axis = {}
y_axis = []
x_result = []
y_result = []

# data = load_csv("paper_data.csv")

# for result in temp_data:
for result in syn_data:
    y_axis.append(float(result[-1]))

for i in range(len(y_axis)):
    idx = math.floor(y_axis[i])
    # print("y_aixs, idx = ", y_axis[i], idx)
    
    if idx in x_axis.keys():
        x_axis[idx] += 1
    else:
        x_axis[idx] = 1

result_list = sorted(x_axis.items(), key=lambda t:t[0])
print(result_list)

for row in result_list:
    x_result.append(row[0])
    y_result.append(row[-1])

print("\n\n\nx : ", x_result)
print("y : ", y_result, "\n\n\n")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([0, 11])
ax.set_xticks(list(range(1, 11, 1)))
# ax.set_yticks(list(range(0, max(y_result)+5, 5)))
plt.plot(x_result, y_result, color = 'k')
plt.bar(x_result, y_result, color = 'y')
plt.xlabel("Scale of Result")
plt.ylabel("Frequency")
plt.title("Data distribution")
plt.show()

####################################################################################################

write_csv("syn_data.csv", syn_data)