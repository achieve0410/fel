from numpy import *
import operator

def classify0(inx, dataset, labels, k):
    iris_dictionary={3:'setosa', 2:'versicolor', 1:'virginica'} ## dictionary로 정의
    datasetSize = dataset.shape[0]
    diffMat = tile(inx, (datasetSize,1)) - dataset
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistindicies = distances.argsort()

    classCount={}
    for i in range(k):
        votellabel = labels[sortedDistindicies[i]]
        classCount[votellabel] = classCount.get(votellabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return iris_dictionary.get(sortedClassCount[0][0]) ## 결과값에 매칭되는 dictionary값으로 반환

def file2matrix(filename):
    iris_dictionary={'I.?setosa':3, 'I.?versicolor':2, 'I.?virginica':1} ## csv file에 정의된 품명을 dictionary로 정의
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)            
    returnMat = zeros((numberOfLines,4))       
    classLabelVector = []                    
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:4]
        classLabelVector.append(iris_dictionary.get(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

irisMat, irisLabels = file2matrix("iris.csv") ## file read

print("\nclassify result :", classify0(([6.7,3.3,5.7,2.2]), irisMat, irisLabels, 5)) ## kNN (k=5)