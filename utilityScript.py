

import numpy
import sys

# running example:
# python utilityScript.py expected.txt real.txt output.txt

def readFileIntoArray(fileName):
    finalData = []
    with open(fileName) as file: 
        data = file.readlines()

        for line in data:
            v = [int(x) for x in line.split(',')] 
            finalData.append(v)
    return finalData

def calculateUtil(latency, cost):
    constVal = 5
    
    if latency > 0 or cost > 0 and latency+cost != 0:
        return (constVal**5)/(latency+cost)
    else:
        return 0


def main(args):
    if len(args)<4:
        print ("file names missing")
    
    expectedFile = args[1]
    realFile = args[2]
    outputFile = args[3]
    
    expectedData = readFileIntoArray(expectedFile)
    realData = readFileIntoArray(realFile)
    
    if  len(expectedData) > len(realData):
        minLen = len(realData)
    else:
        minLen = len(expectedData)
    finalData = []
    for i in range(minLen):
        predictedReal = [calculateUtil(expectedData[i][0],expectedData[i][1]), calculateUtil(realData[i][0],realData[i][1]) ]
        finalData.append(predictedReal)
    
    numpy.savetxt(outputFile, finalData, delimiter=",")

if __name__ == "__main__":
    main(sys.argv)



