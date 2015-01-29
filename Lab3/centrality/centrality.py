# the follwing script calculates two measures of centrality
# (spatial statistics): mean center and central feature
# the input to these stats is the city.txt file
#
# DEFINITIONS
#
# MEAN CENTER: the average x-coordinate and the average
# y-coordinate for all features in the study area
#
# CENTRAL FEATURE: the x,y coordinate of a feature
# having the shortest distance to all features in the study area
# 
#
# author:   Arika Ligmann-Zielinska
# date:     September 21, 2006
# version:  01
# ----------------------------------------------------------------
# [1] to accomplish the task we need: point data, and
# distance calculation

import math

def readPoints(inFile):
    f = open(inFile, 'r')
    body = f.readlines()
    f.close()
    dataPoints = {}
    for row in body:
        dataRow = row.strip().split()
        dataPoints[dataRow[0]] = [float(dataRow[1]), float(dataRow[2])]       
    return dataPoints
    # reads point data from a txt file and returns a dictionary
    # where key is the city name and the coordinates are lists

def meanCenter(points):
    pointList = points.values()
    xList = []
    yList = []
    for i in pointList:
        xList.append(i[0])
        yList.append(i[1])
    avgX = sum(xList)/len(pointList)
    avgY = sum(yList)/len(pointList)
    print "The mean center is at: ", (avgX, avgY)
    # finds the mean center of all the points
    
def distance(pointOne, pointTwo):
    xDif = math.pow(pointOne[0]-pointTwo[0], 2)
    yDif = math.pow(pointOne[1]-pointTwo[1], 2)
    dist = round(math.sqrt(xDif + yDif), 2)
    return dist
    # calculates euclidean distance between two points
    # the points are represented by dictionaries

def centralFeature(points):
    totDistDict = {}
    print "Computing central feature.............."
    print
    for key in points:
        total = 0
        for j in points:
            if key != j:
                total += distance (points[key], points[j])
                total = round(total, 2)
        totDistDict[key] = total
    print "The combined distances of the following points to all others are:", totDistDict
    print
    print "Therefore, the central feature (least total distance) is:", min(totDistDict, key=totDistDict.get)
    # returns the central point from the input points
    

# ----------------------------------------------------------------

pointDict = readPoints("/Users/stephencrook/Documents/Work/SDSU/Courses/Geography 683/Labs/Lab3/centrality/cities.txt")

meanCenter(pointDict)
print
print distance(pointDict["Seattle"], pointDict["San_Diego"])
print
centralFeature(pointDict)
print

hospitalDict = readPoints("/Users/stephencrook/Documents/Work/SDSU/Courses/Geography 683/Labs/Lab3/centrality/hospitals.txt")

meanCenter(hospitalDict)
print
print distance(hospitalDict["6004"], hospitalDict["6028"])
print
centralFeature(hospitalDict)
