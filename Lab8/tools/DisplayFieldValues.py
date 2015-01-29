#Author:    Stephen Crook
#Date:      10/29/2014
#Purpose:   ArcGIS script to display field values.
##################################################################################

import arcpy

fc = arcpy.GetParameterAsText(0)

fieldName = arcpy.GetParameterAsText(1)

#establishes search cursor

rows = arcpy.SearchCursor(fc, "", "", fieldName)

#uses search cursor to cycle through values, printing them out.

numFeat = 0
arcpy.AddMessage("\n\nValues for " + fieldName + ":")
with arcpy.da.SearchCursor(fc, fieldName) as cursor:
    for row in cursor:
        arcpy.AddMessage("{0}".format(str(row[0])))
        numFeat += 1

#gives total number of features based on the counter, above
        
arcpy.AddMessage("\nThe number of features is: " + str(numFeat) + "\n")