# Name: SelectandCalculate.py
# Author: ESRI
# Date: May 21, 2007
# Purpose: To replace repeated processes in the Lynx submodels.
#
# --------------------------------------------------------------

# Import arcgisscripting and sys modules
import arcgisscripting, sys

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Script arguments...
InputFC = sys.argv[1]

if InputFC == gp.scratchworkspace + "\Elevation_FC":

    # Add the utility field and then make a feature layer. 
    gp.AddField(InputFC, "ElevUtil", "short")
    gp.MakeFeatureLayer(InputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based on attribute values
    # in the ElevZone field. Then use the Calculate Field tool to assign a different attribute 
    # value (between 1 and 9) to the ElevUtil field. Finally, clear the selection.
    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " ElevZone >= 14 AND ElevZone <= 20 ")
    gp.CalculateField("Lyr", "ElevUtil", "9")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " ElevZone >= 10 AND ElevZone <= 13 ")
    gp.CalculateField("Lyr", "ElevUtil", "5")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " ElevZone <= 9 ")
    gp.CalculateField("Lyr", "ElevUtil", "1")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " ElevZone >= 21 ")
    gp.CalculateField("Lyr", "ElevUtil", "7")

    gp.SelectLayerByAttribute("Lyr", "CLEAR_SELECTION", "")

    gp.Delete("Lyr")

elif InputFC == gp.scratchworkspace + "\Landforms_FC":

    # Add the utility field and then make a feature layer.
    gp.AddField(InputFC, "LandformUtil", "short")
    gp.MakeFeatureLayer(InputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based on attribute values
    # in the ElevZone field. Then use the Calculate Field tool to assign a different attribute 
    # value (between 1 and 9) to the ElevUtil field. Finally, clear the selection.
    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " LandformCode = 34 " )
    gp.CalculateField("Lyr", "LandformUtil", "5")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " LandformCode = 35 " )
    gp.CalculateField("Lyr", "LandformUtil", "9")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " LandformCode = 36 " )
    gp.CalculateField("Lyr", "LandformUtil", "4")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " LandformCode =  44 " )
    gp.CalculateField("Lyr", "LandformUtil", "8")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " LandformCode = 45 " )
    gp.CalculateField("Lyr", "LandformUtil", "2")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " LandformCode = 48 " )
    gp.CalculateField("Lyr", "LandformUtil", "3")

    gp.SelectLayerByAttribute("Lyr", "CLEAR_SELECTION", "" )

    gp.Delete("Lyr")

elif InputFC == gp.scratchworkspace + "\Squirrel_FC":

    # Add the utility field and then make a feature layer.
    gp.AddField(InputFC, "SquirrelUtil", "short")
    gp.MakeFeatureLayer(InputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based on attribute values
    # in the ElevZone field. Then use the Calculate Field tool to assign a different attribute 
    # value (between 1 and 9) to the ElevUtil field. Finally, clear the selection.
    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 1 " )
    gp.CalculateField("Lyr", "SquirrelUtil", "9")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 2 " )
    gp.CalculateField("Lyr", "SquirrelUtil", "5")

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 0 " )
    gp.CalculateField("Lyr", "SquirrelUtil", "1")

    gp.SelectLayerByAttribute("Lyr", "CLEAR_SELECTION", "" )

    gp.Delete("Lyr")


elif InputFC == gp.scratchworkspace + "\Grouse_FC":

    # Add the utility field and then make a feature layer.
    gp.AddField(InputFC, "GrouseUtil", "short")
    gp.MakeFeatureLayer(InputFC, "Lyr")
    
    # Use the Select Layer By Attribute tool to select features based on attribute values
    # in the ElevZone field. Then use the Calculate Field tool to assign a different attribute 
    # value (between 1 and 9) to the ElevUtil field. Finally, clear the selection.
    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 1 " )
    gp.CalculateField("Lyr", "GrouseUtil", "9" )

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 2 " )
    gp.CalculateField("Lyr", "GrouseUtil", "5" )

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 0 " )
    gp.CalculateField("Lyr", "GrouseUtil", "1" )

    gp.SelectLayerByAttribute("Lyr", "CLEAR_SELECTION", "" )

    gp.Delete("Lyr")


elif InputFC == gp.scratchworkspace + "\Hare_FC":    

    # Add the utility field and then make a feature layer.
    gp.AddField(InputFC, "HareUtil", "short")
    gp.MakeFeatureLayer(InputFC, "Lyr")

    # Use the Select Layer By Attribute tool to select features based on attribute values
    # in the ElevZone field. Then use the Calculate Field tool to assign a different attribute 
    # value (between 1 and 9) to the ElevUtil field. Finally, clear the selection.
    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 1 " )
    gp.CalculateField("Lyr", "HareUtil", "9" )

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 2 " )
    gp.CalculateField("Lyr", "HareUtil", "5" )

    gp.SelectLayerByAttribute("Lyr", "NEW_SELECTION", " HABZONE = 0 " )
    gp.CalculateField("Lyr", "HareUtil", "1" )

    gp.SelectLayerByAttribute("Lyr", "CLEAR_SELECTION", "" )

    gp.Delete("Lyr")

else:
    gp.AddError("Feature class is missing or incorrect.")
