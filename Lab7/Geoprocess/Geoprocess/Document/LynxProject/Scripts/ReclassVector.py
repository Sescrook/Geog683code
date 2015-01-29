#---------------------------------------------------------------------
#ReclassVector.py
#Created on: April 14, 2004
#Purpose: To reclassify values in an attribute field based on user-
#specified ranges. Ranges are specified by entering a break point value
#for each range.  Input data can be a table, table view, feature class
#or a feature layer.
#---------------------------------------------------------------------

# Import system modules
import win32com.client, sys

# Create the Geoprocessor object
gp = win32com.client.Dispatch("esriGeoprocessing.GPDispatch.1")

# Script arguments...
table = sys.argv[1]
OriginalField = sys.argv[2]
BreakPoints = sys.argv[3]
ReclassField = sys.argv[4]

#get a set of all rows in the table
rows  = gp.UpdateCursor(table)
#for each row in the set
row = rows.Next()

while row:
    #get the value from the field with the original values
    originalValue = row.GetValue(OriginalField)
    reclassValue = 1

    #loop through the break point values
    for breakValues in BreakPoints.split(";"):
        breakValues = breakValues.replace("'","")
        #compare each original value to each break point value.
        #if the original value is higher than the break point value,
        #assign it to the class above the break point
        if originalValue > float(breakValues):
            reclassValue = reclassValue + 1
        #otherwise break out of the loop
        #(This will assign the value to the class below the break point)
        else:
            break

    #set the new class value in the field with the reclassed values
    row.SetValue(ReclassField, reclassValue)
    rows.UpdateRow(row)
    row = rows.Next()

del rows
