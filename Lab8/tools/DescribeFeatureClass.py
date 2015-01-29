#Author:    Stephen Crook
#Date:      10/29/2014
#Purpose:   ArcGIS script to describe a feature class.
##################################################################################

import arcpy

descFC = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(descFC)

#checks type of feature class and prints out the type it finds.

if desc.shapeType == "Polyline":
    shapeType = "Polyline"
elif desc.shapeType == "Polygon":
    shapeType = "Polygon"
elif desc.shapeType == "Point":
    shapeType = "Point"
else:
    shapeType = "some other weird shape type"

#adds message about type of feature class
    
arcpy.AddMessage("This feature class' type is: " + shapeType)
    