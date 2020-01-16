#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys
import pandas as pd


# utility = (reward^5)/ (latency+cost)
def calculateUtil(latency, cost, reward = 100):
    
    if latency > 0 or cost > 0 and latency+cost != 0:
        return (reward**5)/(latency+cost)
    else:
        return -1

# this funciton picks up the latency and the cost columns from a csv file
def readUtilityIntoArray(fileName):
    
    
    file = pd.read_csv(fileName)
    latencies = file['Latency']
    costs = file['Cost']
    data = []
    for i in range(len(latencies)):
         data.append(calculateUtil(latencies[i], costs[i]))
        
        
    return data

# calculate the utility of each latency, cost row
def genUtilityDataFrame(realFile, predictedFile):
    realUtility = readUtilityIntoArray(realFile)
    predictedUtility = readUtilityIntoArray(predictedFile)
    
    finalData = list(zip(realUtility, predictedUtility))
#   Create the pandas DataFrame 
    df = pd.DataFrame(finalData,columns=['realUtility', 'predictedUtility']) 
    return df


def main(args):
    if len(args)<4:
        print ("file names missing")
    
    expectedFile = args[1]
    realFile = args[2]
    outputFile = args[3]
   
    realPredictedUtility = genUtilityDataFrame(realFile, expectedFile)

    # writing to file
    realPredictedUtility.to_csv(outputFile)
    
if __name__ == "__main__":
    main(sys.argv)



