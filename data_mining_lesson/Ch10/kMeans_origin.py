'''
Created on Feb 16, 2011
k Means Clustering for Ch10 of Machine Learning in Action
@author: Peter Harrington
'''
from numpy import *

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float, curLine)) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) #la.norm(vecA-vecB)

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n))) #create centroid mat,   k=3 / n=2 
    for j in range(n):#create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:][j])
        rangeJ = float(max(dataSet[:][j])-minJ)
        rd = random.rand(k,1)

        centroids[:, j] = minJ + rangeJ * rd

    return centroids
    
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0] # m = 80
    clusterAssment = mat(zeros((m,2)))#create mat to assign data points 
                                      #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    print("\nRandom centroid: \n", centroids)

    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j][:], dataSet[i][:])
                #print("i, j, distJI : ", i, j, distJI)
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2

        for cent in range(k):#recalculate centroids

            ptInClust = nonzero( clusterAssment[:, 0].A == cent )[0]

            for num in range(len(ptInClust)):
                ptsInClust = dataSet[ptInClust[num]][:]#get all the point in this cluster
                centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean 
    return centroids, clusterAssment

def calculateNumOfClust(clusterAssment, k):

    NumOfClust = mat(zeros((k,1)))

    for index in range(len(clusterAssment)):
        clusteringResult = clusterAssment[index, 0]
        NumOfClust[int(clusteringResult)] = NumOfClust[int(clusteringResult)] + 1
    
    return NumOfClust

# load data from text file
kMeansData = loadDataSet("testSet2.txt")

# set the value of k
k = 7

# execute kMeans clustering algorithm / A = Final centroids, B = point-centroid distance
A, B = kMeans(kMeansData, k)

# print centroid & clusterAssment
print("Final centroids: \n", A)
print("\nClustering Result : \n", B)

# calculate the number of each cluster
NumOfClust = calculateNumOfClust(B, k)
print(NumOfClust)