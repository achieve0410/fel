import csv
import numpy as np
import pandas as pd
import math
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from statsmodels.api import OLS
from statsmodels.regression.linear_model import RegressionResults
from scipy import stats
from sklearn import linear_model


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

## create and summary model
model = OLS(y_train, x_train)
y_pred = model.fit()
print(y_pred.summary())

## predict the answer
pred = y_pred.predict(x_train)
print(pred)

## calculate RSME
line_counter = 0
while 1:
    if len(data)<=line_counter: break

    loss[line_counter][0] = abs( y_train[line_counter][0]-pred[line_counter] )
    line_counter += 1

RSME = math.sqrt( pow(sum(loss),2) )/len(y_train)
print(RSME)