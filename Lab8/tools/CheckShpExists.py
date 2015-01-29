#Author:    Stephen Crook
#Date:      10/29/2014
#Purpose:   ArcGIS script to check if a shapefile exists. If it does not, it is created.

##################################################################################

import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)
checkFC = arcpy.GetParameterAsText(1)

#Checks if shp exists and creates it if it doesn't

if arcpy.Exists(checkFC):
    arcpy.Delete_management(checkFC)
    arcpy.AddMessage(checkFC + ", the specified shapefile has been deleted")
else:
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, checkFC, "POINT")
    arcpy.AddMessage(checkFC + " has been created as a point feature class!")
    
    
    