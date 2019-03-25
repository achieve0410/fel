from numpy import *
import operator
import matplotlib
import os
import matplotlib.pyplot as plt

#########################################################################################

def classify0(inx, dataset, labels, k):
    datasetSize = dataset.shape[0]
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
    returnMat = zeros((numberOfLines,2))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split(',')
        returnMat[index,:] = listFromLine[0:2]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

group, labels = file2matrix("classi.csv")
#print("group\n", group, "\nlabels", labels)

#########################################################################################

## classify0 사용방법
#print("\nclassify result", classify0(([90,85]), group, labels, 3))

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

def file2matrix_2(filename):
    love_dictionary={'largeDoses':3, 'smallDoses':2, 'didntLike':1}
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)            #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        if(listFromLine[-1].isdigit()):
            classLabelVector.append(int(listFromLine[-1]))
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

datingMat, datingLabels = file2matrix_2("datingTestSet.txt")

#print("datingMat", datingMat, "datingLabels", datingLabels)

#########################################################################################

# fig, ax = plt.subplots(1,1)
# ax.scatter(datingMat[:,1], datingMat[:,2],)
# plt.show()

#########################################################################################

def getOrder(labels):
    orderLists = list(set(labels)) ## set: 중복 데이터 제거, list: 재구성
    indexLists = []
    for item in labels:
        indexLists.append(orderLists.index(item) + 1)
    return indexLists
dataingLabelColor = getOrder(datingLabels)

fig, ax = plt.subplots(1,1)
ax.scatter(datingMat[:,0], datingMat[:,1],c=dataingLabelColor)
#plt.show()

#########################################################################################

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

datingMat, datingLabels = file2matrix_2("datingTestSet.txt")
dataingLabelColor = getOrder(datingLabels)
normDataSet, ranges, minVals = autoNorm(datingMat)

hoRatio = 0.10
datingMat, datingLabels = file2matrix_2("datingTestSet.txt")
dataingLabelColor = getOrder(datingLabels)
normMat, ranges, minVals = autoNorm(datingMat)

m = normMat.shape[0]
numTestVecs = int(m*hoRatio)
errorCount=0.0
for i in range(numTestVecs):
    classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:], datingLabels[numTestVecs:m], 11)
    if(classifierResult!=datingLabels[i]):
        errorCount += 1.0
    
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input(\
                                  "percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix_2('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream, ])
    classifierResult = classify0((inArr - minVals)/ranges, normMat, datingLabels, 3)
    print( "You will probably like this person: %s" % resultList[classifierResult - 1])

#classifyPerson()

#########################################################################################

def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

print( img2vector("trainingDigits/0_0.txt"))

#########################################################################################

testFileList = os.listdir("trainingDigits")
print(testFileList)

for i in range(len(testFileList)):
    fileName = testFileList[i]
    print(fileName)

for i in range(len(testFileList)):
    fileStr = testFileList[i]
    imgVector = img2vector("trainingDigits/%s" % fileStr)
    print(fileStr, imgVector)

imageMat = zeros((len(testFileList), 1024))
imageLabel = []

for i in range(len(testFileList)):
    fileStr = testFileList[i]
    imageMat[i, :] = img2vector("trainingDigits/%s" % fileStr)
    fileNameStr = fileStr.split('.')[0]
    classNumStr = int(fileNameStr.split('_')[0])
    print(classNumStr)

#########################################################################################