# 'raster.py'
# defines the Raster class
#
# author:   Arika Ligmann-Zielinska
# date:     October 09, 2008
#
# description:
#   - each "Raster" object has:
#           1. name
#           2. extent
#           3. body of cells
#           4. land cover types frequency table
#           5. dominant land cover
# ----------------------------------------------------------------
# class definition
# ----------------------------------------------------------------

class Raster:
    def __init__ (self, ascii):
        """initiates raster layer from ASCII & remap input files"""
        self.name = ascii                   # raster name
        self.grid = getAsciBody(ascii)      # 2D array of cells (int)
        self.extent = [len(self.grid),\
                       len(self.grid[0])]   #[row, col]
        self.types = self.types()           # list of LC categories
        self.freq = self.iniFreq()          # {type, count}
        self.dominant = -9999               # ini dominant
        print self                          # raster summary

    def __str__(self):
        """raster description"""
        strg = "Raster %s \nSize %d rows %d cols\n"\
              %(self.name, self.extent[0], self.extent[1])
        # %d stands for a decimal integer
        strg = strg + "----------\nDominant type "
        strg = strg + self.nodata() + "\n"
        return strg

    def setFreq(self):
        """claculates land cover frequencies"""
        totCells = float(self.extent[0] * self.extent[1])
        # 'float' is needed for non-integer division below
        types = self.freq.keys()
        # create a 1D list from our grid
        cells = [cell for row in self.grid for cell in row]
        cells.sort()
        typeNum = 0
        for t in types:
            for cell in cells:
                if cell == t:
                    typeNum = typeNum + 1
            typeNum = typeNum/totCells*100
            self.freq[t] =typeNum
            typeNum = 0
        print "Frequencies updated"
        
    def setDominant(self):
        """returns the dominant land cover type """
        domCover = max(self.freq.values())
        for type in self.freq.keys():
            if self.freq[type] == domCover:
                self.dominant = type
                # what is the potential problem here?
                # ...how about ties? or the NODATA value?

    def nodata(self):
        """ returns a string of dominant"""
        if self.dominant == -9999:
            return "NODATA"
        return str(self.dominant)

    def types(self):
        """ exhaustive & mutually exclusive list of categories """
        # refer to types.py for details
        # create a 1D list from our grid
        items = [cell for row in self.grid for cell in row]
        items.sort()
        categories = [items[0]] # init a list of types
        for item in items:
            if categories[-1] < item:
                categories.append(item)
        return categories

    def iniFreq(self):
        """ initiates the frequency table {lc_id: freq}"""
        fTable = {}
        for c in self.types:
            fTable[c] = -9999 # default NODATA
        return fTable
                
# ----------------------------------------------------------------
# auxiliary functions
# ----------------------------------------------------------------        

def getAsciBody(ascii):
    """ converts ASCII file body to a 2D array"""
    f = open(ascii, 'r')
    body = f.readlines()
    f.close()
    grid = body[6:] # get rid of ASCII header
    # the body is now a list of strings - one str per row
    # we need to convert it to a list
    # of lists of integers - 2Darray
    # where, 2Darray[row][col] -> grid cell value
    lattice = [] # initialize 2Darray
    for row in grid:
        row = row.strip() # del '\n' special character
        latticeRow = map(int, row.split())
                # split the row to str, map the str to int
        lattice.append(latticeRow) # add row to lattice
    return lattice

