# Name: CheckForField.py
# Author: ESRI
#       Updated By: Nicole Simons, nesimons@gmail.com
# Date: May 21, 2007
#       Update Date: October 10, 2012
# Purpose: Check if a field exists, then take the appropriate
#          branch in the model.
# Version: 10.1, Python 2.7
#
# --------------------------------------------------------------

# Import arcpy and sys modules
import arcpy, sys

# Script arguments...
inputFC = arcpy.GetParameterAsText(0)

#Declare a boolean value to determine if the field exists. Its value
#is set to false as it is assumed that the field does not exist until
#the input data is checked.
bFieldExists = False

# Get the fields from the input feature class
fields = arcpy.ListFields(inputFC, "*", "ALL")

# Check to see if the field exists or not
for field in fields:
    fldName = field.name
    if (fldName == "HabitatUtil"):
        bFieldExists = True

# If the field exists, the value for the first derived output parameter
# is set to true.
if bFieldExists == True:
    arcpy.AddMessage("The field exists")
    arcpy.SetParameterAsText(1, "True")
    arcpy.SetParameterAsText(2, "False")

# If the field doesn't exist, the value for the second derived output
# parameter is set to true.
else:
    arcpy.AddMessage("The field does not exist")
    arcpy.SetParameterAsText(1, "False")
    arcpy.SetParameterAsText(2, "True")
