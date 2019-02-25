import csv
import math
import numpy as np
from sklearn.ensemble import RandomForestClassifier

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

## set train & test data
x_train = np.zeros( [len(temp_data), len(temp_data[0])-1] )
y_train = np.zeros( [len(temp_data), 1] )
x_test = np.zeros( [len(temp_data), len(temp_data[0])-1] )
y_test = np.zeros( [len(temp_data), 1] )

pred = np.zeros( [len(temp_data), 1] )
loss = np.zeros( [len(temp_data), 1] )

## variables for array
line_counter = 0
compo_counter = 0

## temp_data to train/test data ( list (1 dim.) -> array (2 dim.) )
while 1:
    data = temp_data
    if len(data)<=line_counter: break

    if compo_counter == 3:
        y_train[line_counter][0] = data[line_counter][compo_counter]
        line_counter += 1
        compo_counter = 0

    else :
        x_train[line_counter][compo_counter] = data[line_counter][compo_counter]
        compo_counter += 1

## reshape datasets
np.reshape(x_train, (-1, 1))
np.reshape(y_train, (1, -1))

## create RF model
model = RandomForestClassifier(criterion='entropy', n_estimators=10, n_jobs=2, random_state=1)
model.fit(x_train, y_train.ravel())

## predict n print the estimated values
y_pred = model.predict(x_train)

## calculate RSME
line_counter = 0
while 1:
    if len(data)<=line_counter: break

    loss[line_counter][0] = abs( y_train[line_counter][0]-y_pred[line_counter] )
    line_counter += 1

RSME = math.sqrt( pow(sum(loss),2) )/len(y_train)
print("RSME : ", RSME)