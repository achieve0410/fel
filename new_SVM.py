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

def separate_data(myData):

    line_count = 0
    compo_count = 0

    x_data = np.zeros( [len(myData), len(myData[0])-1] )
    y_data = np.zeros( [len(myData), 1] )

    while 1:
        data = myData
        if len(data)<=line_count: break

        if compo_count == len(data[0])-1:
            y_data[line_count][0] = int(float(data[line_count][compo_count]))
            compo_count = 0
            line_count += 1
        else :
            x_data[line_count][compo_count] = int(data[line_count][compo_count])
            compo_count += 1
    
    return x_data, y_data

def generateRandomNum(data, num):
    myList = []

    while 1:
        if(len(myList)>=num): break
        randNum = random.randrange(0, len(data))

        if randNum in myList:
            continue
        else: myList.append(randNum)

    return myList

# train_data = load_csv("syn_data/50000/syn_data_1.csv")
test_data = load_csv("modified_data.csv")

numOfTrain = [10000, 20000, 50000, 100000, 200000]
result = []

for i in numOfTrain:
    
    trainName = "syn_data/data_" + str(i) + ".csv"
    train_data = load_csv(trainName)

    x_train, y_train = separate_data(train_data)
    x_test, y_test = separate_data(test_data)

    print(i, ": ", len(x_train), len(y_train), len(x_test), len(y_test))

    pred = np.zeros( [len(test_data), 1] )
    loss = np.zeros( [len(test_data), 1] )

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


## after visualization
####################################################################################################
# x_axis = {}
# y_axis = []
x_result = numOfTrain
print(x_result)
y_result = result
print(y_result)

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