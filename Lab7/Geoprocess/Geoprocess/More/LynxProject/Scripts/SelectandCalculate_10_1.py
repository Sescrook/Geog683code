# Name: SelectandCalculate.py
# Author: ESRI
#       Update By: Nicole Simons
#       Update V2 By: Tyler Packett 
# Date: May 21, 2007
#       Update Date: October 10, 2012
#       Update Date V2: October 20, 2012
# Purpose: To replace repeated processes in the Lynx submodels.
#
# --------------------------------------------------------------

# Import arcpy and sys module
import arcpy, sys

# Script arguments...
inputFC = arcpy.GetParameterAsText(0)

if inputFC == arcpy.env.scratchWorkspace + "\\Elevation_FC":

    # Add the utility field and then make a feature class
    arcpy.AddField_management(inputFC, "ElevUtil", "short")
    arcpy.MakeFeatureLayer_management(inputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based
    # on attribute values in the ElevZone field. Then use the Calculate
    # Field tool to assign a different attribute value (between 1 & 9)
    # to the ElevUtil field. Finally, clear the selection.
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " ElevZone >= 14 AND ElevZone <= 20")
    arcpy.CalculateField_management("Lyr", "ElevUtil", "9")

    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " ElevZone >= 10 AND ElevZone <= 13")
    arcpy.CalculateField_management("Lyr", "ElevUtil", "5")

    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " ElevZone <= 9")
    arcpy.CalculateField_management("Lyr", "ElevUtil", "1")

    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " ElevZone >= 21")
    arcpy.CalculateField_management("Lyr", "ElevUtil", "7")

    arcpy.SelectLayerByAttribute_management("Lyr", "CLEAR_SELECTION", "")

    arcpy.Delete_management("Lyr")

elif inputFC == arcpy.env.scratchWorkspace + "\\Landforms_FC":

    # Add the utility field and then make a feature layer
    arcpy.AddField_management(inputFC, "LandformUtil", "short")
    arcpy.MakeFeatureLayer_management(inputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based
    # on attribute values in the ElevZone field. Then use the Calculate
    # Field tool to assign a different attribute value (between 1 & 9)
    # to the ElevUtil field. Finally, clear the selection.
    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " LandformCode = 34")
    arcpy.CalculateField_management("Lyr", "LandformUtil", "9")

    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " LandformCode = 36")
    arcpy.CalculateField_management("Lyr", "LandformUtil", "5")

    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " LandformCode = 44")
    arcpy.CalculateField_management("Lyr", "LandformUtil", "8")

    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " LandformCode = 45")
    arcpy.CalculateField_management("Lyr", "LandformUtil", "2")

    arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", " LandformCode = 48")
    arcpy.CalculateField_management("Lyr", "LandformUtil", "3")

    arcpy.SelectLayerByAttribute_management("Lyr", "CLEAR_SELECTION", "")

    arcpy.Delete_management("Lyr")

elif inputFC == arcpy.env.scratchWorkspace + "\\Squirrel_FC":

    # Add the utility field and then make a feature layer
    arcpy.AddField_management(inputFC, "SquirrelUtil", "short")
    arcpy.MakeFeatureLayer_management(inputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based
    # on attribute values in the ElevZone field. Then use the Calculate
    # Field tool to assign a different attribute value (between 1 & 9)
    # to the ElevUtil field. Finally, clear the selection.
    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 1 " )
    arcpy.CalculateField_management("Lyr", "SquirrelUtil", "9")

    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 2 " )
    arcpy.CalculateField_management("Lyr", "SquirrelUtil", "5")

    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 0 " )
    arcpy.CalculateField_management("Lyr", "SquirrelUtil", "1")

    arcpy.SelectLayerByAttribute_management("Lyr", "CLEAR_SELECTION", "" )

    arcpy.Delete_management("Lyr")

elif inputFC == arcpy.env.scratchWorkspace + "\\Grouse_FC":
    # Add the utility field and then make a feature layer.
    arcpy.AddField_management(inputFC, "GrouseUtil", "short")
    arcpy.MakeFeatureLayer_management(inputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based
    # on attribute values in the ElevZone field. Then use the Calculate
    # Field tool to assign a different attribute value (between 1 & 9)
    # to the ElevUtil field. Finally, clear the selection.
    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 1 " )
    arcpy.CalculateField_management("Lyr", "GrouseUtil", "9" )

    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 2 " )
    arcpy.CalculateField_management("Lyr", "GrouseUtil", "5" )

    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 0 " )
    arcpy.CalculateField_management("Lyr", "GrouseUtil", "1" )

    arcpy.SelectLayerByAttribute_management("Lyr", "CLEAR_SELECTION", "" )

    arcpy.Delete_management("Lyr")

elif inputFC == arcpy.env.scratchWorkspace + "\\Hare_FC":

    # Add the utility field and then make a feature layer.
    arcpy.AddField_management(inputFC, "HareUtil", "short")
    arcpy.MakeFeatureLayer_management(inputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based
    # on attribute values in the ElevZone field. Then use the Calculate
    # Field tool to assign a different attribute value (between 1 & 9)
    # to the ElevUtil field. Finally, clear the selection.
    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 1 " )
    arcpy.CalculateField_management("Lyr", "HareUtil", "9" )

    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 2 " )
    arcpy.CalculateField_management("Lyr", "HareUtil", "5" )

    arcpy.SelectLayerByAttribute_management("Lyr", "NEW_SELECTION", " HABZONE = 0 " )
    arcpy.CalculateField_management("Lyr", "HareUtil", "1" )

    arcpy.SelectLayerByAttribute_management("Lyr", "CLEAR_SELECTION", "" )

    arcpy.Delete_management("Lyr")

else:
    arcpy.AddError("Feature class is missing or incorrect")
