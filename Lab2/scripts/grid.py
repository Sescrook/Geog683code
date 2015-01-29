# This scripts stores functions for calculating grid statistics
#
#
# SKILLS:
#       1. defining functions
#       2. using functions
#       3. building user modules
#
# Author: Arika Ligmann-Zielinska
# date: September 19, 2006
# version 01
# FUNCTION DEFINITIONS-----------------------------------------

# NOTE: for all the examples that follow input grid (inGrid)
# is a 2D array = a list of lists of integers

def gridRows(inGrid):
    # returns the number of rows in grid
    return len(inGrid)

def gridCols(inGrid):
    # returns the number of columns in grid
    return len(inGrid[0])
    
def gridSize(inGrid):
    # returns the total number of cells in grid
    rows = gridRows(inGrid)
    cols = gridCols(inGrid)
    return rows*cols
      
def gridSum(inGrid):
    # returns the sum of all grid values
    grid1D = []
    for row in inGrid:
        grid1D = grid1D + row
    sumOfGrid = 0
    for item in grid1D:
        sumOfGrid = sumOfGrid + item
    return sumOfGrid

# Put your function definitions below. Note that I already
# specified the input parameters for the functions.
# You are encouraged not to add any more parameters (those
# provided are enough to perform a given function calculation).
# Note that you may use (call) one function you have
# already built in another function.
# When you are working on a specific function, start from deleting
# its 'pass' keyword 

def gridAvg(inGrid):
    #returns average of the numbers in thge grid
    gridAverage = float(gridSum(inGrid)) / float(gridSize(inGrid))
    return gridAverage

def gridMin(inGrid):
    # returns the min of all grid values
    flatGrid = [image for i in inGrid for image in i]
    return min(flatGrid)
    

def gridMax(inGrid):
    # returns the max of all grid values
    flatGrid = [image for i in inGrid for image in i]
    return max(flatGrid)

def gridValueRange(inGrid):
    # returns the range of grid values
    gridRange = gridMax(inGrid)-gridMin(inGrid)
    return gridRange

def gridValueAtXY(inGrid, x=0, y=0):
    # returns the value at position (x,y) in a grid, default is (0,0)
    flatGrid = [image for i in inGrid for image in i]
    cols = len(inGrid[0])  # col num
    selCell = (x) + (cols * (y))
    return flatGrid[selCell]
    

def printGrid(inGrid):
    # prints the grid to display
    tup = enumerate(inGrid)
    tupList = [list(elem) for elem in tup]
    for i in range(len(tupList)):
        print "The values for row " + str(tupList[i][0]) + " are " + str(tupList[i][1])

# FUNCTION TESTING ---------------------------------------------

# sample grid:
smallGrid =  [[1,2,0,1],
              [0,2,3,2],
              [1,0,0,3],
              [2,0,0,0]]

# sample position

x = 1
y = 2
 
# functions invocation

rows = gridRows(smallGrid)
print "the number of rows", rows
print
cols = gridCols(smallGrid)
print "the number of cols", cols
print
size = gridSize(smallGrid)
print "total number of cells", size
print
gsum = gridSum(smallGrid)
print "grid value total", gsum
print
gave = gridAvg(smallGrid)
print "the average of the grid is", gave
print
gmin = gridMin(smallGrid)
print "the minimum value is", gmin
print
gmax = gridMax(smallGrid)
print "the maximum value is", gmax
print
grange = gridValueRange(smallGrid)
print "the range of the values is", grange
print
print "the value at X=1, Y=1 is", gridValueAtXY(smallGrid, 1, 1)
print
printGrid(smallGrid)


# do the same for the functions avg,min,max,range you defined above
# also display the value for the given position using gridValueAtXY
# finally, display the whole grid using printGrid

