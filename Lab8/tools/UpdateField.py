#Author:    Stephen Crook
#Date:      10/29/2014
#Purpose:   ArcGIS script to add a new field to a feature class and update the values based on two other concatenated values.
##################################################################################


import arcpy

fc = arcpy.GetParameterAsText(0)
inField1 = arcpy.GetParameterAsText(1)
inField2 = arcpy.GetParameterAsText(2)
newName = arcpy.GetParameterAsText(3)

#adds a field to the feature class based on the name specified in the dialog

try:
    arcpy.AddField_management(fc, newName, "TEXT")
    arcpy.AddMessage("New field created")
except:
    arcpy.GetMessages(2)

#update cursor established, loops through rows of the new field updating with the concatenated values

cursor = arcpy.UpdateCursor(fc)

for row in cursor:
    row.setValue(newName, str(row.getValue(inField1)) + " " + str(row.getValue(inField2)))
    cursor.updateRow(row)

arcpy.AddMessage("New fields values have been added")

