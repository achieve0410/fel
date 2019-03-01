import json
import math
import numpy as np
from sklearn.svm import SVC

## int -> string (transfer integer to string for key)
def first_key_trans(line_counter):
    return_string = str(line_counter)
    return return_string

## int -> string (transfer integer to string for key)
def second_key_trans(compo_counter):
    if compo_counter==0:
        return_string = 'compliance'
    elif compo_counter==1:
        return_string = 'acceleration'
    elif compo_counter==2:
        return_string = 'deceleration'
    else:
        return_string = 'result'
    
    return return_string


## parsing data from json file
with open('test.json') as json_file:

    ## preparing data
    json_data = json.load(json_file)

    ## variables for array
    line_counter = 0
    compo_counter = 0

    ## set train & test data
    x_train = np.zeros( [len(json_data["data"]), len(json_data["data"]["0"])-1] )   ## [182, 3]
    y_train = np.zeros( [len(json_data["data"]), 1] )                               ## [182, 1]
    x_test = np.zeros( [len(json_data["data"]), len(json_data["data"]["0"])-1] )    ## [182, 3]
    y_test = np.zeros( [len(json_data["data"]), 1] )                                ## [182, 1]

    pred = np.zeros( [len(json_data["data"]), 1] )                                  ## [182, 1]
    loss = np.zeros( [len(json_data["data"]), 1] )                                  ## [182, 1]

    ## json_data to train/test data ( list (1 dim.) -> array (2 dim.) )
    while 1:
        data = json_data["data"]
        if len(data)<=line_counter: break

        ## find key for parsing data from json file
        first_key = first_key_trans(line_counter)
        second_key = second_key_trans(compo_counter)

        if compo_counter == 3:
            y_train[line_counter][0] = data[first_key][second_key]
            line_counter += 1
            compo_counter = 0

        else :
            x_train[line_counter][compo_counter] = data[first_key][second_key]
            compo_counter += 1

## reshape datasets
np.reshape(x_train, (-1, 1))
np.reshape(y_train, (-1, 1))

## create SVM model
model = SVC(kernel='linear', C=1.0, random_state=0)
model.fit(x_train, y_train.ravel())

## predict n print the estimated values
y_pred = model.predict(x_train)

## calculate RSME
line_counter = 0
while 1:
    if len(data)<=line_counter: break

    loss[line_counter][0] = abs( y_train[line_counter][0]-y_pred[line_counter] )
    line_counter += 1

RSME = math.sqrt( sum( pow(loss, 2) ) / len(y_train) )
print("RSME : ", RSME)