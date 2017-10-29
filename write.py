from point import readtxt
from arcpy import env
import os
import arcpy
path = r'path\to\workspace'
env.workspace = path
env.overwriteOutput = True
point = 'starky9.shp'
def readall(a):
    fields_name =['UTMGrid', 'UGEast', 'UGNorth', 'Ids', 'STime', 'GMDate', 'GMTime', 'LocDate', 'LocTime', 'RadNum', 'Species', 'UTME', 'UTMN', 'Year', 'Grensunr', 'Grensuns', 'Obswt'] #readtxt(os.path.join(path,'Starkey2.txt'))
    print fields_name
    with open(a,'r') as g:
        listss = list()
        c=0
        for d,i in enumerate(g.readlines()):
                value =  i.split(',')
                listss.append(value)
        cursor = arcpy.da.UpdateCursor(point,fields_name)
        for index,row in enumerate(cursor):
            print index
            for j in range(len(value)):
                row[j]=listss[index][j]
                cursor.updateRow(row)
            print 'finshed row'+str(index)
if __name__ =='__main__':
    readall(os.path.join(path,'Starkey3.txt'))
