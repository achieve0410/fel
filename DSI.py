from scipy import stats
import csv
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

## Empty array for save dataset
temp_header = []
temp_data = []
real_data = np.array([])
train_data = np.array([])
test_data = np.array([])

line_counter = 0

with open('driving_score_180ea.csv') as f:
    while 1:
        data = f.readline().replace("\n","")
        # print(data)
        if not data: break
        if line_counter == 0:
            temp_header = data.split(",") # 
        else:
            temp_data.append(data.split(","))
        line_counter = line_counter + 1
        
print(type(temp_header))
print(temp_header)

print(temp_data)










# ## open csv file and save dataset
# f = open('driving_score_180ea.csv', 'r', encoding='utf-8')
# csvReader = csv.reader(f)

# for row in csvReader:
#     temp_data.append(row)

# f.close()



# for row in range(1, len(temp_data)):
#     np.append(real_data, temp_data[row])

# print(temp_data[1])

# print( real_data )

# for row in range(1, len(data)):
#    for col in range(0, len(data[0])-1):
#        train_data.append(data[row][col])
#        if( (col+1)%3 == 0):
#            test_data.append(data[row][col+1])
#            continue

# np.reshape(train_data, (-1, 1))
# np.reshape(test_data, (1, -1))

# regr = linear_model.LinearRegression()

# regr.fit(train_data, test_data)

# y_pred = regr.predict(train_data)

# print('Coef. : \n', regr.coef_)
# print("MSE : %.2f" % mean_squared_error(test_data, y_pred))


#print( "train_data : " , train_data )
#print( "test_data : " , test_data )

#print( len(train_data) )
#print( len(test_data) )
