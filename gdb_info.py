import arcpy, os, traceback, sys
import numpy as np

# PARAMETERS - set gdb as current workspace
arcpy.env.workspace = arcpy.GetParameterAsText(0)





# Create a text file with the name of the gdb being analyzed
gdb_name = arcpy.env.workspace.split('\\')[-1][0:-4]
text_out = open(gdb_name + ".txt", "a")

