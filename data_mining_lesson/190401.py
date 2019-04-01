# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt

# fig = plt.figure(1)
# plt.plot([2,3])
# plt.plot([1,4])
# plt.axis([0, 1, 0.5, 4.5])
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('two lines')

# fig.savefig('plot.svg')

##############################################################

# import matplotlib.pyplot as plt
# plt.figure(1, figsize=(10, 10))
# ax = plt.subplot(111)

# ax.annotate("test", xy=(0.2,0.2), xycoords='data', xytext=(0.8, 0.8), textcoords='data', arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),)
# plt.show()

##############################################################

# import matplotlib.pyplot as plt
# plt.figure(1, figsize=(10, 10))
# ax = plt.subplot(111)

# ax.annotate("test", xy=(0.2,0.2), xycoords='data', xytext=(0.8, 0.8), textcoords='data',
#             size=20, va="center", ha="center", arrowprops=dict(arrowstyle="<->", connectionstyle="angle3, angleA=90, angleB=0"),)
# plt.show()

##############################################################

import numpy as np
from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt

dset, dlabels = createDataSet()
ent = calcShannonEnt(dset)
print("\n\n\n", ent)

#######################################

# labels = []
# for featVec in dset:
#     labels.append(featVec[-1])
# labelSet = set(labels)
# label = np.array(labelSet)
# print(label)

# for featVec in dataSet:

#######################################

def splitDataset(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

splitdset = splitDataset(dset, 0, 1) ## 0번째 축의 value가 1인 경우, 1인 row를 뽑아낸 후 0번째 축 없애기
print(splitdset)

#######################################