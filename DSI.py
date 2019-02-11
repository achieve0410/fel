from scipy import stats
import csv

## Empty array for save dataset
data = []

## open csv file and save dataset
f = open('cluster_origin_2.csv', 'r', encoding='utf-8')
csvReader = csv.reader(f)

for row in csvReader:
    data.append(row)

f.close()



print( len(data) )

# for line in rdr:
#     print(line)
# f.close()

# x = [5.05, 6.75, 3.21, 2.66]
# y = [1.65, 26.5, -5.93, 7.96]

# gradient, intercept, r_value, p_value, std_err = stats.linregress(x,y)
# print( "Gradient and intercept" , gradient, intercept )

# print( "R-squared", r_value**2 )
# print( "p-value", p_value )