#Author:    Stephen Crook
#Date:      10/29/2014
#Purpose:   ArcGIS script to describe a raster.
##################################################################################

import arcpy

descRast = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(descRast)

#describes extent of the raster

arcpy.AddMessage("Raster extent is: " + str(desc.extent))

#tells type of raster: float or integer

if desc.isInteger == True:
    arcpy.AddMessage("This raster is an integer")
else:
    arcpy.AddMessage("This raster is a float")
