import math

numPoints = raw_input("How many points are in your path?")
xList = []
yList = []

#fills in lists of x and y values with user supplied values
for i in range(int(numPoints)):
    x = int(raw_input("What is the X coordinate of point " + str(i+1) + "?"))
    y = int(raw_input("What is the Y coordinate of point " + str(i+1) + "?"))
    xList.append(x)
    yList.append(y)
print "Your points are as follows: "
for i in range(int(numPoints)):
    print "(" + str(xList[i]) + "," + str(yList[i]) + ")"

#modified distance function from previous labs
def distance(x1, x2, y1, y2):
    xDif = math.pow(x2 - x1, 2)
    yDif = math.pow(y2 - y1, 2)
    dist = round(math.sqrt(xDif+yDif), 2)
    return dist

totDist = 0.0

#uses distance between each point in sequence and adds to the total distance
for i in range(int(numPoints)-1):
    thisDist = distance(xList[i], xList[i+1], yList[i], yList[i+1])
    totDist += thisDist

#reports total distance
print "The total distance is", totDist


