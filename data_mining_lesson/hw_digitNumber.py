from numpy import *
import operator
import os

## k-NN classification
def classify0(inx, dataset, labels, k):                                          
    ## calculate distance and find argument array
    datasetSize = dataset.shape[0]
    diffMat = tile(inx, (datasetSize,1)) - dataset
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistindicies = distances.argsort()

    classCount={}
    for i in range(k): ## repeat k to vote label
        votellabel = labels[sortedDistindicies[i]]
        classCount[votellabel] = classCount.get(votellabel, 0) + 1

    ## sort vote result
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

## insert digit data into vector
def img2vector(filename):                                                        
    returnVect = zeros((1,32*32))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

## classifier for digit number
def digitNumberClassifier(k, trainingdir, testdir):                              
    ## set directory of training data
    trainingFileList = os.listdir('%s' % trainingdir)
    trainingMat = zeros((len(trainingFileList),32*32))                           ## digit number data
    digitNumberLabels = []                                                       ## list for label of digit number data

    for i in range(len(trainingFileList)):
        fileString = trainingFileList[i]                                         ## 0_0.txt, 0_1.txt, 0_2.txt, ...
        fileNameString = fileString.split('.')[0]                                ## 0_0, 0_1, 0_2, ...
        classNumString = int(fileNameString.split('_')[0])                       ## 0, 0, 0, ... => label
        digitNumberLabels.append(classNumString)                                 ## append to label list
        trainingMat[i,:] = img2vector("%s/%s" % (trainingdir, fileString))       ## insert data of digit number

    ## set directory of test data
    testFileList = os.listdir('%s' % testdir)
    error = 0.0

    for i in range(len(testFileList)):
        fileString = testFileList[i]                                             ## 0_0.txt, 0_1.txt, 0_2.txt, ... 
        fileNameString = fileString.split('.')[0]                                ## 0_0, 0_1, 0_2, ...
        classNumString = int(fileNameString.split('_')[0])                       ## 0, 0, 0, ... => label(answer)
        unknownDigitNumber = img2vector("%s/%s" % (testdir, fileString))         ## unknown digit number data

        ## predict value using k-NN classification
        classificationResult = classify0(unknownDigitNumber, trainingMat, digitNumberLabels, k)         
        #print( "Predict value: %d, Answer: %d" % (classificationResult, classNumString))

        ## calculate and alert error if wrong
        if (classificationResult != classNumString): 
            #print("Wrong!\n")
            error += 1.0                                                                                
    
    ## print error n error rate
    print("\n###########################################################\n")
    print("                     Result in %d-NN" % k)
    print( "\n  # of total data : %d" % len(testFileList), "\n  # of error : %d" % error)
    print( "\n  Error rate : %f" % (100*error/(len(testFileList))), "%")
    print("\n###########################################################")
    
    return error

## execute digitNumber classifier n find the best k
errorArray = zeros(14)
for i in range(1,15):
    print("\n\n\nExecute %d-NN..." % i)
    errorArray[i-1] = digitNumberClassifier(i, "trainingDigits", "testDigits")
print("\n\n\nThe best k : %d [# of error : %d]" % (errorArray.argmin()+1, errorArray[errorArray.argmin()]))
