# defines the City class
# SKILLS:
#       1. class definition
#       2. building user modules
#
# author:   Arika Ligmann-Zielinska
# first created: October 16, 2005
# version 02: September 19, 2006
#
# description:
#   - each "City" object has:
#           1. name
#           2. position (x, y)
#   - each "City" object can:
#           1. be created
#           2. describe itself
#           3. calculate distance between itself and other city
# ----------------------------------------------------------------
# imports
# ----------------------------------------------------------------
import math # for calculating distance
# ----------------------------------------------------------------
# class definition
# ----------------------------------------------------------------
class City:
    def __init__ (self, name, x, y):
        # constructs city
        self.name = name
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return "Your city name is " + self.name + " located at X=" + str(self.x) + " and Y=" + str(self.y)
        # describes city
        # write some description string here
        # and then return it

    
    def distance(self, other):
        # calculates euclidean distance between two cities
        distX = math.pow(self.x - other.x, 2)
        distY = math.pow(self.y - other.y, 2)
        return math.sqrt(distX + distY)
        # do the same for Y coordinate
        # then use the sqrt function (also in math module)
        # to return the distance
        
# ----------------------------------------------------------------
# testing section
# ----------------------------------------------------------------

if  __name__ == "__main__":
    cityOne = City("La Mesa", 100, 10)
    cityTwo = City("Carlsbad", 100, 80)
    print "testing..."

print City.__str__(cityOne)
print City.distance(cityOne, cityTwo)
print City.distance(cityTwo, cityOne)

    # print the cities (their descriptions)

    # now calculate the distance between cityOne and cityTwo
    # using the distance method
    # display the result in some meaningful way (i.e using some
    # descriptive sentence)


