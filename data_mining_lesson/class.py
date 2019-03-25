def classify0(inx, dataset, labels, k):
    datasetSize = dataset.shape[0]
    #print datasetSize
    diffMat = tile(inx, (datasetsize,1)) - dataset
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistindicies = distances.argsort()

    classCount={} ## dictionary type
    for i in range(k):
        votellabel = labels[sortedDistindicies[i]]
        classCount[votellable] = classCount.get(votellabel, 0) + 1 ## 투표한 값이 없으면 1, 있으면 기존값+1
    sortedClassCount = sorted(classCount.items(), key=itemgetter(1), reverse=True) ## .items : dictionary를 순서쌍으로 바꿔줌
    return sortedClassCount[0][0]

## set하고 dictionary는 순서와 상관이 없다

def createDataset():
    group = array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
    labels = ['a', 'a', 'b', 'b']
    return group, labels
a, b = createDataset():

%matplotlib inline

import matplotlib.pyplot as plt

## annotating 공부 필요

plt.plot([1,2,3,4])
plt.plot([1,2,3,4], [3,6,11,18])
plt.plot([1,2,3,4], [3,6,11,18], linewidth=2.0)
plt.plot([1,2,3,4], [3,6,11,18], 'ro')
plt.plot([1,2,3,4])
plt.plot([1,2,3,4])
plt.plot([1,2,3,4])

###############################################################
# 3     104 R
# 2     100 R
# 1      81 R
# 101    10 A
# 9       5 A
# 98      2 A
# 18     90 ?