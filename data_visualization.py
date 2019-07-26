from matplotlib import pyplot as plt
import math
import csv

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

x_axis = {}
y_axis = []
x_result = []
y_result = []

data = load_csv("paper_data.csv")

for result in data:
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
