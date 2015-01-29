#Author:    Stephen Crook
#Date:      10/29/2014
#Purpose:   ArcGIS script to list feature classes.
##################################################################################

import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)

#creates list of feature classes

allFC = arcpy.ListFeatureClasses()
arcpy.AddMessage("\nThe feature classes in the workspace are: \n")

#prints out each feature class in the list established above
                 
for fc in allFC:
    arcpy.AddMessage(fc)

lenNum = str(len(allFC))
arcpy.AddMessage("There are " + lenNum + " feature classes here \n")