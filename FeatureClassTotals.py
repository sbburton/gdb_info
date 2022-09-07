# Author: Case Robertson
# This script counts all Feature Classes (FC) in a Geodatabase for both Vectors and Rasters

import arcpy
import sys
from arcpy import env
#arcpy.env.workspace = "C:\GData\EXAMPLE.gdb"
arcpy.env.workspace = arcpy.GetParameterAsText(0)

# Get stand alone FCs
vectorFCcount = len(arcpy.ListFeatureClasses("",""))

# Count Rasters
rasterFCcount = len(arcpy.ListRasters("",""))

# Get list of Feature Datasets and loop through them
fds = arcpy.ListDatasets("","")
for fd in fds:
    oldws = arcpy.env.workspace
    arcpy.env.workspace = oldws + "\\" + fd
    vectorFCcount = vectorFCcount + len(arcpy.ListFeatureClasses("",""))
    arcpy.env.workspace = oldws

# Add a message to ArcGIS
arcpy.AddMessage(str(vectorFCcount) + " Vector Feature Classes, " + str(rasterFCcount) + " Rasters")

# Create a text file in the workspace
text_file = open("EXAMPLE.txt", "w")
text_file.write(str(vectorFCcount) + " Vector Feature Classes, " + str(rasterFCcount) + " Rasters");
text_file.close()