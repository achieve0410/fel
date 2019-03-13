import pymysql
import math
import numpy as np
from statsmodels.api import OLS

## connect to MySQL
conn = pymysql.Connect(host='172.17.0.3', user='wh', password='root',
                    db='driving_score', charset='utf8')

## Create Cursor
curs = conn.cursor()

## execute SQL query
sql = "select * from data;"
curs.execute(sql)

## Fetch data
rows = curs.fetchall()

## preparing data
json_data = rows

## disconnect to MySQL
conn.close()

## variables for array
line_counter = 0
compo_counter = 0

## set train & test data
x_train = np.zeros( [len(json_data), len(json_data[0])-1] )   ## [182, 3]
y_train = np.zeros( [len(json_data), 1] )                     ## [182, 1]
x_test = np.zeros( [len(json_data), len(json_data[0])-1] )    ## [182, 3]
y_test = np.zeros( [len(json_data), 1] )                      ## [182, 1]

pred = np.zeros( [len(json_data), 1] )                        ## [182, 1]
loss = np.zeros( [len(json_data), 1] )                        ## [182, 1]

## json_data to train/test data ( list (1 dim.) -> array (2 dim.) )
while 1:
    data = json_data
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
np.reshape(y_train, (-1, 1))

## create and summary model
model = OLS(y_train, x_train)
y_pred = model.fit()
#print(y_pred.summary())

## predict the answer
pred = y_pred.predict(x_train)

## calculate RSME
line_counter = 0
while 1:
    data = json_data
    if len(data)<=line_counter: break

    loss[line_counter][0] = abs( y_train[line_counter][0]-int(pred[line_counter]) )
    line_counter += 1

RSME = math.sqrt( sum( pow(loss, 2) ) / len(y_train) )
print("RSME : ", RSME)

