from numpy import *
import matplotlib.pyplot as plt

def classify0(inx, dataset, labels, k):
    datasetSize = dataset.shape[0]
    #print datasetSize
    diffMat = tile(inx, (datasetSize,1)) - dataset
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistindicies = distances.argsort()

    classCount={} ## dictionary type
    for i in range(k):
        votellabel = labels[sortedDistindicies[i]]
        classCount[votellabel] = classCount.get(votellabel, 0) + 1 ## 투표한 값이 없으면 1, 있으면 기존값+1
    sortedClassCount = sorted(classCount.items(), key=itemgetter(1), reverse=True) ## .items : dictionary를 순서쌍으로 바꿔줌
    return sortedClassCount[0][0]

## set하고 dictionary는 순서와 상관이 없다

def createDataset():
    group = array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['R', 'R', 'R', 'A', 'A', 'A']
    return group, labels
group, labels = createDataset()
print(group, labels)
########################################################################################################################

label = asarray([labels]).reshape(-1,1)
group_add_label = hstack((group, label))

##############################################

fig, ax = plt.subplots(1,1)
i = 0

# while(1):
#     if(i>=len(group_add_label)):
#         break
#     if(group_add_label[i][2]=='R'):
#         ax.plot(group_add_label[i,0], group_add_label[i,1], 'bo')
#     elif(group_add_label[i][2]=='A'):
#         ax.plot(group_add_label[i,0], group_add_label[i,1], 'go')
#     i += 1
while(1):
    if(i>=len(group_add_label)):
        break
    if(group_add_label[i][2]=='R'):
        ax.plot(group[i,0], group[i,1], 'bo')
    elif(group_add_label[i][2]=='A'):
        ax.plot(group[i,0], group[i,1], 'go')
    i += 1

ax.plot([18],[90], 'ro')
plt.show()

##############################################

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)            #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)   
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat,classLabelVector

##############################################
    # ## annotating 공부 필요

    # plt.plot([1,2,3,4])
    # plt.plot([1,2,3,4], [3,6,11,18])
    # plt.plot([1,2,3,4], [3,6,11,18], linewidth=2.0)
    # plt.plot([1,2,3,4], [3,6,11,18], 'ro')
    # plt.plot([1,2,3,4])
    # plt.plot([1,2,3,4])
    # plt.plot([1,2,3,4])

#########################

# 3     104 R
# 2     100 R
# 1      81 R
# 101    10 A
# 9       5 A
# 98      2 A
# 18     90 ?