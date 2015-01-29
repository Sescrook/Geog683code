# runs the city application
#
# SKILLS:
#       1. using classes
#       2. reading data from a file
#
# author:   Arika Ligmann-Zielinska
# first created: October 16, 2005
# version 02: September 19, 2006
#
# description:
#       1. reads a flat table of city attributes to a list of
#          city objects
#       2. returns distances between cities
# -----------------------------------------------------------------
# imports
# -----------------------------------------------------------------
from city import City
# -----------------------------------------------------------------
# auxiliary functions
# -----------------------------------------------------------------

def setCities(inFile):
    # puts city.txt content into City class objects
    # the field order of input file is: name x y
    f = open(inFile, 'r')
    body = f.readlines()
    f.close()
    cities = []  # list of cities
    for row in body:
        cityData = row.strip().split()
        cityName = cityData[0]
        cityX = cityData[1]
        cityY = cityData[2]
        newCity = City(cityName, cityX, cityY)
        cities.append(newCity)
        print 
    return cities

# -----------------------------------------------------------------
# application main code
# -----------------------------------------------------------------

cityList = setCities("/Users/stephencrook/Documents/Work/SDSU/Courses/Geography 683/Labs/Lab2/scripts/cities.txt")

##testing how to access data in cityList...
##for i in range (len(cityList)):
##    print cityList[i].name
##    print cityList[i].x
##    print cityList[i].y
##    print cityList[i].distance(cityList[i+1])

for i in range (len(cityList)):
    for j in range (len(cityList)):
        if i != j:                      #nobody cares about the distance the city is from itself
            print "The distance between", cityList[i].name + " and", cityList[j].name +\
            " is:", cityList[i].distance(cityList[j])

# create a list of cities using the setCities function above 
# calculate and display the distance between each pair of cities
# using for example two 'for' loops
# possible result: see the sample run in Lab 3 handout



