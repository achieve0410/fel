import numpy as np
from math import log
import operator

## open file and return data as list format
def file2matrix(filename): 
    f = open(filename)
    arrayOLines = f.readlines()
    f.close()
    returnMat = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat.append(listFromLine[0:5])
        index += 1
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate'] ## labeling
    return returnMat, lensesLabels

## calculate Shannon's Entropy
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: ## voting
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts: ## calculate Entropy
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

## split dataset after choice appropriate feature
def splitDataset(dataSet, axis, value): 
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value: ## except feature where featVec[axis] equals value
            reducedFeatVec = featVec[:axis] ## start ~ axis-1
            reducedFeatVec.extend(featVec[axis+1:]) ## axis+1 ~ end
            retDataSet.append(reducedFeatVec)
    return retDataSet

## choose the best feature for which split the dataset
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet) ## origin Entropy
    bestInfoGain = 0.0
    bestFeature = -1

    ## calculate infoGain
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataset(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet) ## calculate subTree's Entropy
        infoGain = baseEntropy - newEntropy ## infoGain = origin Entropy - subTrees's Entropy

        if infoGain > bestInfoGain: ## chosen Best feature by infoGain result
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

## create tree structure
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): ## if dataset have only one label, not split
        return classList[0]
    if len(dataSet[0])==1: ## if decision is not made after remain one feature
        return majorityCnt(classList)
    
    ## choose best feature and delete it
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}} ## add feature in the tree
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        ## make new subTree
        myTree[bestFeatLabel][value] = createTree(splitDataset(dataSet, bestFeat, value), subLabels)
    return myTree

## if decision is not made, proceed with a majority vote 
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reversed=True)
    return sortedClassCount[0][0]

## read data from text file and create myTree
dataSet, labels = file2matrix("lenses.txt")
treeResult = createTree(dataSet, labels)

## print myTree result
print(treeResult)

