# Name: ReclassVector.py
# Author: ESRI
#       Update By: Nicole Simons, nesimons@gmail.com
# Date: May 21, 2007
#       Update Date: October 10, 2012
# Purpose: To reclassify values in an attribute field based on user-
#          specified ranges. Ranges are specified by entering a break 
#          point value for each range.  Input data can be a table,
#          table view, feature class or a feature layer.
#
# -------------------------------------------------------------------

# Import the arcpy and sys modules
import arcpy, sys

# Script Arguments...
table = arcpy.GetParameterAsText(0)
originalField = arcpy.GetParameterAsText(1)
breakPoints = arcpy.GetParameterAsText(2)
reclassField = arcpy.GetParameterAsText(3)

# Get a set of all rows in the table
fields = (originalField,reclassField)
with arcpy.da.UpdateCursor(table, fields) as cursor:
    for row in cursor:
        # Get the value from the field with the original values
        originalValue = row[0]
        reclassValue = 1
        row[1] = reclassValue
        for breakValues in breakPoints.split(";"):
            breakValues = breakValues.replace("'","")
            # Compare each original value to each break point value.
            # If the original value is higher than the break point
            # value, assign it to the class above the break point
            if originalValue > float(breakValues):
                reclassValue = reclassValue + 1
                row[1] = reclassValue
            # otherwise break out of the loop
            # (This will assign the value to the class below the break
            # point
            else:
                break
        # Set the new class value in the field with the reclassed values
        cursor.updateRow(row)
