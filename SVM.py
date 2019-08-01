import csv
import math
import random
import numpy as np
from matplotlib import pyplot as plt
from sklearn.svm import SVC

## Empty list for save dataset
temp_data = []

def load_csv(filepath):
    data = []
    line_count = 0
    with open(filepath, encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        for row in reader:
            data.append(row)
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
                y_train[line_count_tr][0] = int(float(data[line_count][compo_count]))
                compo_count = 0
                line_count_tr += 1
                line_count += 1
            else :
                x_train[line_count_tr][compo_count] = int(data[line_count][compo_count])
                compo_count += 1

        else:
            if compo_count == len(data[0])-1:
                y_test[line_count_ts][0] = int(float(data[line_count][compo_count]))
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

temp_data = load_csv("syn_data/2200/syn_data_3.csv")
resultArr = []

for rep in range(1, 220):
    numberOfTest = 10*rep
    print(numberOfTest)

    result = []
    for i in range(10):
        randNumList = generateRandomNum(temp_data, numberOfTest)

        x_train, y_train, x_test, y_test = separate_data(temp_data, randNumList)

        print(len(x_train), len(y_train), len(x_test), len(y_test))

        pred = np.zeros( [len(temp_data), 1] )
        loss = np.zeros( [len(temp_data), 1] )

        ## reshape datasets
        # np.reshape(x_train, (-1, 1))
        # np.reshape(y_train, (-1, 1))

        ## create SVM model
        model = SVC(kernel='linear', C=1.0, random_state=0)
        model.fit(x_train, y_train.ravel())

        ## predict n print the estimated values
        y_pred = model.predict(x_test)

        ## calculate RMSE
        line_count = 0
        while 1:
            data = x_test
            if len(data)<=line_count: break

            # print("y_test, y_pred : ", y_test[line_count][0], y_pred[line_count])

            loss[line_count][0] = abs( y_test[line_count][0]-y_pred[line_count] )
            line_count += 1

        RMSE = math.sqrt( sum( pow(loss, 2) ) / len(y_test) )
        result.append(RMSE)
    # print("RSME : ", result, sum(result)/10)
    print("AVG RMSE: ", sum(result)/10)
    resultArr.append(sum(result)/10)


## after visualization
####################################################################################################
# x_axis = {}
# y_axis = []
x_result = list(range(10, 2200, 10))
print(x_result)
y_result = resultArr

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# ax.set_xticks(list(range(10, 51, 10)))
# ax.set_yticks(list(range(0, max(y_result)+5, 5)))
plt.plot(x_result, y_result, color = 'k')
plt.bar(x_result, y_result, color = 'y')
plt.xlabel("# of Test data")
plt.ylabel("Average RMSE")
plt.title("Result")
plt.show()

####################################################################################################