#Author:    Stephen Crook
#Date:      10/29/2014
#Purpose:   ArcGIS script to list fields.
##################################################################################

import arcpy

fc = arcpy.GetParameterAsText(0)

#gets a list of fields

fieldList = arcpy.ListFields(fc)

#prints out each field in the list of fields

for i in fieldList:
    arcpy.AddMessage("%s is type %s, with a length of %i" % (i.name, i.type, i.length))


arcpy.AddMessage("\nIn total, there are " + str(len(fieldList)) + " fields\n")