import csv
import math
import random
from matplotlib import pyplot as plt
import numpy as np
from statsmodels.api import OLS

## Empty list for save dataset
temp_data = [] 

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

def separate_data(myData, randNumList):

    line_count = 0
    compo_count = 0
    line_count_tr = 0
    line_count_ts = 0

    x_train = np.zeros( [len(myData)-len(randNumList), len(myData[0])-1] )
    y_train = np.zeros( [len(myData)-len(randNumList), 1] )
    x_test = np.zeros( [len(randNumList), len(myData[0])-1] )
    y_test = np.zeros( [len(randNumList), 1] )

    while 1:
        data = myData
        if len(data)<=line_count: break

        if line_count not in randNumList:
            if compo_count == len(data[0])-1:
                y_train[line_count_tr][0] = (float(data[line_count][compo_count]))
                compo_count = 0
                line_count_tr += 1
                line_count += 1
            else :
                x_train[line_count_tr][compo_count] = int(data[line_count][compo_count])
                compo_count += 1

        else:
            if compo_count == len(data[0])-1:
                y_test[line_count_ts][0] = (float(data[line_count][compo_count]))
                compo_count = 0
                line_count_ts += 1
                line_count += 1
            else :
                x_test[line_count_ts][compo_count] = int(data[line_count][compo_count])
                compo_count += 1
    
    return x_train, y_train, x_test, y_test

def generateRandomNum(data, num):
    myList = []

    while 1:
        if(len(myList)>=num): break
        randNum = random.randrange(0, len(data))

        if randNum in myList:
            continue
        else: myList.append(randNum)

    return myList

def getResultNum(originData, data):

    minValue = 999
    retNum = 0
    for row in originData:
        temp_sum = 0
        for i in range(len(row)-1):
            diff = abs(int(row[i]) - data[i])
            temp_sum += diff
        
        if minValue >= temp_sum:
            minValue = temp_sum
            retNum = float(row[-1])
        
    return retNum

def generateSyntheticData(originData):
    data = []

    for i in range(8):
        if i >= 2:
            randomNum = random.randint(1, 10)
        else:
            randomNum = random.randint(0, 9)
        data.append(randomNum)
    
    randomNum = getResultNum(originData, data)
    data.append(randomNum)

    return data

## load data from csv file
temp_data = load_csv("paper_data.csv")
# print(len(temp_data))


## before visualization
# ####################################################################################################
# x_axis = {}
# y_axis = []
# x_result = []
# y_result = []

# # data = load_csv("paper_data.csv")

# for result in temp_data:
#     y_axis.append(float(result[-1]))

# for i in range(len(y_axis)):
#     idx = math.floor(y_axis[i])
#     # print("y_aixs, idx = ", y_axis[i], idx)
    
#     if idx in x_axis.keys():
#         x_axis[idx] += 1
#     else:
#         x_axis[idx] = 1

# result_list = sorted(x_axis.items(), key=lambda t:t[0])
# print(result_list)

# for row in result_list:
#     x_result.append(row[0])
#     y_result.append(row[-1])

# print("\n\n\nx : ", x_result)
# print("y : ", y_result, "\n\n\n")

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.set_xlim([0, 11])
# ax.set_xticks(list(range(1, 11, 1)))
# ax.set_yticks(list(range(0, max(y_result)+5, 5)))
# plt.plot(x_result, y_result, color = 'k')
# plt.bar(x_result, y_result, color = 'y')
# plt.xlabel("Scale of Result")
# plt.ylabel("Frequency")
# plt.title("Data distribution")
# plt.show()

# ####################################################################################################








## generate random data
genNum = 100
for i in range(genNum):
    mylist = generateSyntheticData(temp_data)
    temp_data.append(mylist)
# print(len(temp_data))
# print(temp_data)







## after visualization
####################################################################################################
x_axis = {}
y_axis = []
x_result = []
y_result = []

# data = load_csv("paper_data.csv")

for result in temp_data:
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
ax.set_yticks(list(range(0, max(y_result)+5, 5)))
plt.plot(x_result, y_result, color = 'k')
plt.bar(x_result, y_result, color = 'y')
plt.xlabel("Scale of Result")
plt.ylabel("Frequency")
plt.title("Data distribution")
plt.show()

####################################################################################################









# numberOfTest = 190

# result = []
# for i in range(10):
#     randNumList = generateRandomNum(temp_data, numberOfTest)

#     x_train, y_train, x_test, y_test = separate_data(temp_data, randNumList)

#     # print(x_train, y_train, x_test, y_test)

#     pred = np.zeros( [len(temp_data), 1] )
#     loss = np.zeros( [len(temp_data), 1] )

#     ## reshape datasets
#     # np.reshape(x_train, (-1, 1))
#     # np.reshape(y_train, (-1, 1))

#     ## create and summary model
#     model = OLS(y_train, x_train)
#     y_pred = model.fit()

#     ## predict n print the estimated values
#     pred = y_pred.predict(x_test)

#     ## calculate RMSE
#     line_count = 0
#     while 1:
#         data = x_test
#         if len(data)<=line_count: break

#         # print("y_test, y_pred : ", y_test[line_count][0], pred[line_count])

#         loss[line_count][0] = abs( y_test[line_count][0]-pred[line_count] )
#         line_count += 1

#     RMSE = math.sqrt( sum( pow(loss, 2) ) / len(y_test) )
#     result.append(RMSE)
# print("RSME : ", result, sum(result)/10)