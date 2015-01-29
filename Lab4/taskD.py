#brings in the script used to load a raster in without its header
import raster
import numpy

#imports the specific rasters for attractiveness and price
attract = raster.getAsciBody("attractiveness.txt")
price = raster.getAsciBody("price.txt")

#displays the rasters for attractiveness and price
print
print "attractiveness raster:"
for i in range(len(attract)):
    print attract[i]
print
print "price raster:"
for i in range(len(price)):
    print price[i]
    
#asks for weights
print
weightA = float(raw_input("What is the weight for attractiveness (0.0-1.0)?"))
print
weightP = float(raw_input("What is the weight for price (0.0-1.0)?"))
print

#multiplies values by weights
weightedA = []
weightedP = []
for i in attract:
    smallListweight = []
    for j in i:
        x = j * weightA
        smallListweight.append(x)
    weightedA.append(smallListweight)
for i in price:
    smallListweight = []
    for j in i:
        x = j * weightP
        smallListweight.append(x)
    weightedP.append(smallListweight)

#prints out weights values as check (can delete later)
print "the weighted attractiveness values are as follows:"
for i in range(len(attract)):
    print weightedA[i]
print
print "The weighted price values are as follows:"
for i in range(len(price)):
    print weightedP[i]

#adds two arrays together to find priority values and puts in new array
priorityList = numpy.add(weightedA, weightedP)

print
print "The total utility of each cell based on specified weights are:"
for i in priorityList:
    print i

# find max priority, if there is more than one with that priority, or num 2 highest priority
maxValue = numpy.max(priorityList)
print "The highest value is", maxValue
print

numberMax = 0

for i in numpy.nditer(priorityList):
    if i == maxValue:
        numberMax += 1 #adds to number max counter

#finds second highest value if there is only 1 "maximum value".
#if two (or more) have same maximum values, secondMax is set as maximum value
if numberMax > 1:
    print "Multiple sites tie for having the maximum value of", maxValue
    secondMax = maxValue
else:
    maxRemoved = []
    for i in numpy.nditer(priorityList):
        if i < maxValue:
            maxRemoved.append(i)
    secondMax = numpy.max(maxRemoved)
    print "The second highest value is", secondMax
print
print "######################FINAL RESULTS#############################"
    
#uses numpy to find coordinates of the highest and second highest values
bestPixel = numpy.where(priorityList == maxValue)
secondbestPixel = numpy.where(priorityList == secondMax)
bestPixelX = bestPixel[0]
bestPixelY = bestPixel[1]
secondbestPixelX = secondbestPixel[0]
secondbestPixelY = secondbestPixel[1]
print
if secondMax == maxValue:
    print "The pixels with highest values are:"
    for i in range(len(bestPixelX)):
        print (bestPixelX[i], bestPixelY[i])
    print "Choose these two (or two from this list)!"
else:
    print "The pixel with the highest value is (choose this location):"
    for i in range(len(bestPixelX)):
        print (bestPixelX[i], bestPixelY[i])
    print
    print "And the pixel(s) with the second highest values is/are:"
    for i in range(len(secondbestPixelX)):
        print (secondbestPixelX[i], secondbestPixelY[i])
    print "So choose one of these!"
