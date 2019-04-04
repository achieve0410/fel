import numpy as np

def createDataSet():
    dataSet = [['yes', 'yes', 'yes'],
               ['yes', 'yes', 'yes'],
               ['yes', 'no', 'no'],
               ['no', 'yes', 'no'],
               ['no', 'yes', 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

def transform(dataSet): ## 'yes', 'no' values are mapping to 1, 0 values 
    word_dic = {'yes': 1, 'no': 0} ## define dictionary
    retDataSet = np.array(dataSet).transpose() ## origin data form : 5row 3col => transpose : 3row 5col
    firstFeatureList = []
    secondFeatureList = []
    
    for featVec in dataSet:
        firstFeature = featVec[0] ## first col ; surfaces
        secondFeature = featVec[1] ## second col ; flippers
        firstFeatureList.append(word_dic.get(firstFeature)) ## append to list
        secondFeatureList.append(word_dic.get(secondFeature)) ## append to list

    retDataSet[0] = firstFeatureList ## replace first feature ; surfaces
    retDataSet[1] = secondFeatureList ## replace second feature ; flippers

    return retDataSet.transpose() ## return dataSet after transpose

dset, label = createDataSet() ## create dataSet and labels
print("\nBefore dataSet : \n", dset)
rtds = transform(dset) ## transform values

print("\nAfter dataSet : \n", rtds) ## print replacing result




