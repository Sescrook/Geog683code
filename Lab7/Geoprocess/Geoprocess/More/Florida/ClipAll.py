# Name: ClipAll.py
# Author: ESRI
#       updated by: Nicole Simons
# Date: May 21, 2007
#       updated: October 10, 2012
# Purpose: Clips all of the feature classes in a workspace (e.g. folder, geodatabase or feature dataset)
#          and puts the clipped feature classes in a specified workspace. The name of the output feature
#          classes willbe based on the name of the input feature class name.
#
# Usage: ClipAll.py <input workspace> <clip feature class> <output feature class>
#
# ------------------------------------------------------------------------------------------------------

# Import the arcpy, sys, and os modules
import arcpy, sys, os

# To run, this script requires 3 arguments:
# full pathnames required if InputWS, ClipFC & OutputWS are in different locations
# if in same location, only InputWS requires full pathname

# Argument 1 identifies the input workspace where the input
# feature classes are stored
inputWS = arcpy.GetParameterAsText(0)

# Argument 2 identifies the feature class you'll use to clip
# the input features
clipFC = arcpy.GetParameterAsText(1)
  
# Argument 3 identifies the output workspace where the clipped
# feature classes will be saved
outputWS = arcpy.GetParameterAsText(2)

# Set the current workspace
arcpy.env.workspace = inputWS

# Create a variable that gets a list of all feature classes in the input workspace
fcs = arcpy.ListFeatureClasses("*", "all")

# Loop through the list of feature classes in the input workspace
# clip them with the clip feature class and store them in the
# output workspace
for fc in fcs:
    # Set the output name for each feature class to be the same
    # as the input but stores it in the output workspace
    outputName = outputWS + "\\" + fc
    # Print each clipping operation to the screen
    print "clipping", fc, "with", clipFC, "to produce", outputName
    arcpy.Clip_analysis(fc, clipFC, outputName, "")

# End of script


