from numpy import *
import operator
import os

#########################################################################################

def classify0(inx, dataset, labels, k):
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
    return sortedClassCount[0][0]

#########################################################################################

def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

#########################################################################################

def digitNumberClassifier(k):

    ## set directory of training data
    trainingFileList = os.listdir('trainingDigits')
    trainingMat = zeros((len(trainingFileList),32*32))                           ## digit number data
    digitNumberLabels = []                                                       ## list for label of digit number data

    for i in range(len(trainingFileList)):
        fileString = trainingFileList[i]                                         ## 0_0.txt, 0_1.txt, 0_2.txt, ...
        fileNameString = fileString.split('.')[0]                                ## 0_0, 0_1, 0_2, ...
        classNumString = int(fileNameString.split('_')[0])                       ## 0, 0, 0, ...
        digitNumberLabels.append(classNumString)                                 ## append to label list
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileString)          ## insert data of digit number

    ## set directory of test data
    testFileList = os.listdir('testDigits')
    error = 0.0

    for i in range(len(testFileList)):
        fileString = testFileList[i]                                             ## 0_0.txt, 0_1.txt, 0_2.txt, ... 
        fileNameString = fileString.split('.')[0]                                ## 0_0, 0_1, 0_2, ...
        classNumString = int(fileNameString.split('_')[0])                       ## 0, 0, 0, ...
        unknownDigitNumber = img2vector('testDigits/%s' % fileString)            ## unknwon digit number data

        ## kNN classification and print result
        classificationResult = classify0(unknownDigitNumber, trainingMat, digitNumberLabels, k)         
        print( "Predict value: %d, Answer: %d" % (classificationResult, classNumString))

        ## alert and calculate error if wrong
        if (classificationResult != classNumString): 
            print("Wrong!\n")
            error += 1.0                                                                                
    
    ## print error n error rate
    print("\n###########################################################\n")
    print("                     Result in %d-NN" % k)
    print( "\n  # of total data : %d" % len(testFileList), "\n  # of error : %d" % error)
    print( "\n  Error rate : %f" % (100*error/(len(testFileList))), "%")
    print("\n###########################################################")

#########################################################################################

digitNumberClassifier(3)