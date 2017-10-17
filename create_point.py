import arcpy
import numpy
from arcpy import env
env.workspace = r"C:\Users\11422\Desktop"
env.overwriteOutput = True
dtype=[('x', '=i8'), ('y', '=i8')]
array=numpy.loadtxt(r'C:\Users\11422\Desktop\stak1.txt', delimiter=',', usecols=(0, 1), dtype=[('x', '=i4'), ('y', '=i4')])
print array
fc = r"C:\Users\11422\Desktop\starky10.shp"
arcpy.da.NumPyArrayToFeatureClass(array, fc, ("x", "y"))
print 'finshed'
