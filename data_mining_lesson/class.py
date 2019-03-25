from numpy import *
import operator
import matplotlib.pyplot as plt

#########################################################################################

def classify0(inx, dataset, labels, k):
    datasetSize = dataset.shape[0]
    print("inx", inx)
    print("datasetSize", datasetSize)
    print("dataset", dataset)
    diffMat = tile(inx, (datasetSize,1)) - dataset
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistindicies = distances.argsort()

    classCount={} ## dictionary type
    for i in range(k):
        votellabel = labels[sortedDistindicies[i]]
        classCount[votellabel] = classCount.get(votellabel, 0) + 1 ## 투표한 값이 없으면 1, 있으면 기존값+1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) ## .items : dictionary를 순서쌍으로 바꿔줌
    return sortedClassCount[0][0]

#########################################################################################

def createDataset():
    group = array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['R', 'R', 'R', 'A', 'A', 'A']
    return group, labels

#group, labels = createDataset()
#print(group, labels)

#########################################################################################

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)            #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split(',')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

group, labels = file2matrix("classi.csv")
print(group, labels)

#########################################################################################

## classify0 사용방법
print(classify0(([90,85]), group[:,0:2], labels, 3))

#########################################################################################


#########################################################################################
# ## label을 group과 합치기
# label = asarray([labels]).reshape(-1,1)
# group_add_label = hstack((group, label))

# ## plot
# fig, ax = plt.subplots(1,1)
# i = 0

# while(1):
#     if(i>=len(group_add_label)):
#         break
#     ## Romance일 경우 Blue
#     if(group_add_label[i][2]=='R'):
#         ax.plot(group[i,0], group[i,1], 'bo')
    
#     ## Action일 경우 Green
#     elif(group_add_label[i][2]=='A'):
#         ax.plot(group[i,0], group[i,1], 'go')
#     i += 1

# ## 새로운 점은 Red
# ax.plot([18],[90], 'ro')
# plt.show()

#########################################################################################