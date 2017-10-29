import arcpy
import numpy
from arcpy import env
env.workspace = r"path\to\workspace"
env.overwriteOutput = True
array=numpy.loadtxt(r'path\to\workspace\stak1.txt', delimiter=',', usecols=(0, 1), dtype=[('x', '=i4'), ('y', '=i4')])
print array
fc = r"path\to\workspace\starky10.shp"
arcpy.da.NumPyArrayToFeatureClass(array, fc, ("x", "y"))
print 'finshed'
