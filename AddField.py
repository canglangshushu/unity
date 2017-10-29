import os
from arcpy import env
import arcpy
env.workspace = r"path\to\workspace"
env.overwriteOutput = True
path = r'path\to\workspace'
point = 'starky10.shp'
def readtxt(a):
    with open(a,'r')as g :
        c =  g.readline()
        for i in c.split(','):
            arcpy.AddField_management(point,i,"TEXT")
        fields_name = [f.name for f in arcpy.ListFields(point)]
        print fields_name


if __name__ =='__main__':
    readtxt(os.path.join(path,'Starkey2.txt'))
