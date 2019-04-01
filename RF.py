import csv
import math
import numpy as np
from sklearn.ensemble import RandomForestClassifier

## Empty list for save dataset
train_header = []
train_data = []
test_header = []
test_data = []

## variable for count # of lines
line_counter = 0

## read data from csv file
with open('driving_score_train9.csv') as f:
    while 1:
        data = f.readline().replace("\n","")
        # print(data)
        if not data: break
        if line_counter == 0:
            train_header = data.split(",") # 
        else:
            train_data.append(data.split(","))
        line_counter = line_counter + 1

## variable for count # of lines
line_counter = 0

## read data from csv file
with open('driving_score_test9.csv') as f:
    while 1:
        data = f.readline().replace("\n","")
        # print(data)
        if not data: break
        if line_counter == 0:
            test_header = data.split(",") # 
        else:
            test_data.append(data.split(","))
        line_counter = line_counter + 1

## set train & test data
x_train = np.zeros( [len(train_data), len(train_data[0])-1] )
y_train = np.zeros( [len(train_data), 1] )
x_test = np.zeros( [len(test_data), len(test_data[0])-1] )
y_test = np.zeros( [len(test_data), 1] )

pred = np.zeros( [len(test_data), 1] )
loss = np.zeros( [len(test_data), 1] )

## variables for array
line_counter = 0
compo_counter = 0

## temp_data to train data ( list (1 dim.) -> array (2 dim.) )
while 1:
    data = train_data
    if len(data)<=line_counter: break

    if compo_counter == 7:
        y_train[line_counter][0] = float(data[line_counter][compo_counter])
        line_counter += 1
        compo_counter = 0

    else :
        x_train[line_counter][compo_counter] = float(data[line_counter][compo_counter])
        compo_counter += 1

## reset variable
line_counter = 0
compo_counter = 0

## temp_data to test data ( list (1 dim.) -> array (2 dim.) )
while 1:
    data = test_data
    if len(data)<=line_counter: break

    if compo_counter == 7:
        y_test[line_counter][0] = float(data[line_counter][compo_counter])
        line_counter += 1
        compo_counter = 0

    else :
        x_test[line_counter][compo_counter] = float(data[line_counter][compo_counter])
        compo_counter += 1

## reshape datasets
np.reshape(x_train, (-1, 1))
np.reshape(y_train, (-1, 1))

## create RF model
model = RandomForestClassifier(criterion='entropy', n_estimators=10, n_jobs=2, random_state=1)
model.fit(x_train, y_train.ravel())

## predict n print the estimated values
y_pred = model.predict(x_test)

## calculate RSME
line_counter = 0
while 1:
    data = test_data
    if len(data)<=line_counter: break

    loss[line_counter][0] = abs( y_train[line_counter][0]-y_pred[line_counter] )
    line_counter += 1

RSME = math.sqrt( sum( pow(loss, 2) ) / len(y_train) )
print("RSME : ", RSME)