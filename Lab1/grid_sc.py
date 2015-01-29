# the following script calculates a number of statistics based
# on a predefined 2-dimensional array (grid)
#
# SKILLS:
#       1.looping
#       2.the 'list' object
#       3.built-in functions
#
# Author: Arika Ligmann-Zielinska
# date: September 10, 2006
# version 01
#
# INPUT ------------------------
grid = [[1,1,2,4,1,7,1,7,6,9],\
        [1,2,5,3,9,1,1,1,9,1],\
        [7,4,5,1,8,1,2,0,0,4],\
        [1,4,1,1,1,1,1,1,8,5],\
        [9,0,0,0,0,0,1,1,9,8],\
        [7,4,2,1,8,2,2,2,9,7],\
        [7,4,2,1,7,1,1,1,0,5],\
        [3,4,5,3,4,5,9,1,0,9],\
        [0,0,5,1,1,1,9,7,7,7]]

print
print "Our grid *********************"

for i in grid:
        print i
        
# SIZE -------------------------
rows = len(grid)     # row num
cols = len(grid[0])  # col num
celNum = rows * cols  # cell num

print
print "Number of rows", rows
print "Number of cols", cols
print "Number of cells", celNum
print


flatGrid = [image for i in grid for image in i]
gridSum = sum(flatGrid)
gridSumFloat = float(gridSum)
numCellFloat = float(rows*cols)
gridAve = gridSumFloat/numCellFloat

print "The sum of values in the grid is: " + str(gridSum)
print "The average value is: " + str(gridAve)

# SUM & AVERAGE ----------------

#****** PUT YOUR CODE HERE *****

## hint:
## the easiest way to calculate
## the stats is to convert the
## 2D grid into a 1D array (list)

## calcluate sum and average and
## display the values
    
# MIN & MAX, RANGE -------------

print
print "The minimum value is: " + str(min(flatGrid))
print "The maximum value is: " + str(max(flatGrid))
gridRange = max(flatGrid)-min(flatGrid)
print "The range of values is: " + str(gridRange)
print

print "And here is the whole list of values..." + str(flatGrid)
print

#****** PUT YOUR CODE HERE *****
## find min, max
## calculate range
## display the values

# SELECTED ROW -----------------

rowID = 1 # user input

if rowID > rows - 1 or rowID < 0:
    print "Row index out of range"
    print "Setting to default -> the 1st row"
    rowID = 0
    
selectedRow = grid[rowID]

print "row", rowID, "values:",
print selectedRow

# SELECTED COL -----------------
print
selCol = raw_input("Which column would you like to view?")
startNum = int(selCol)
thisCol = []
for i in range(startNum, celNum,cols):
        thisCol.append(flatGrid[i])
print thisCol

#****** PUT YOUR CODE HERE *****
## display values for a column
## selected by the user
## similar to SELECTED ROW above


# SELECTED CELL VALUE -----------

inCol = int(raw_input("What x coordinate do you want?"))  # X coord - user input
inRow = int(raw_input("What y coordinate do you want?")) # Y coord - user input

if (inCol > cols - 1 or inCol < 0) or \
   (inRow > rows - 1 or inRow < 0):
    print "Cell coordinates out of range"
    print "Setting to default -> (0,0)"
    inCol = 0
    inRow = 0

selCell = (inCol) + (cols * (inRow)) #put the selection num here"
print "The value of the desired cell (" + str(inCol) + "," + str(inRow) + ") is " + str(flatGrid[selCell])
                   
# PUT YOUR CODE HERE *****

# ROW -> VALUE PAIRS -----------

tup = enumerate(grid)
tupList = [list(elem) for elem in tup]
print
for i in range(len(tupList)):
        print "The values for row " + str(tupList[i][0]) + " are " + str(tupList[i][1])

        
#****** PUT YOUR CODE HERE *****

## use the 'enumerate' function
## to display row id and the
## corresponding row values for
## all rows in the grid
