#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:38:52 2018

@author: ekkylli

Code for saving all layers of GeoPackage as separate files
"""
import os
from osgeo import gdal, ogr


#Settings
#Set working dir and output folder
#wrkDir = '/wrk/ekkylli/paituli'
wrkDir = '/wrk/ekkylli/mtk/data/vektori/ogiir/data'
os.chdir(wrkDir)

#OutputFolder
outFolder='layers'

#Check that the folder exists
if not os.path.exists(outFolder):
    os.makedirs(outFolder)
    
#os.chdir(outFolder)
    
#Emtpy the folder
#files = glob.glob(TKoutFolder + '\*')
#for f in files:
#    os.remove(f)


#Make error messages visible
gdal.UseExceptions() #Fail when can't open!
def gdal_error_handler(err_class, err_num, err_msg):
    errtype = {
            gdal.CE_None:'None',
            gdal.CE_Debug:'Debug',
            gdal.CE_Warning:'Warning',
            gdal.CE_Failure:'Failure',
            gdal.CE_Fatal:'Fatal'
    }
    err_msg = err_msg.replace('\n',' ')
    err_class = errtype.get(err_class, 'None')
    print ('Error Number: %s' % (err_num))
    print ('Error Type: %s' % (err_class))
    print ('Error Message: %s' % (err_msg))
 
 #Enable error handler    USE THIS FIRST TO SEE THE ERRORS, remove late for faster throughput
 #It seems that some field width warnings are given when actual data is ok.
#gdal.PushErrorHandler(gdal_error_handler)    
 
 #Disable error handler
#gdal.PopErrorHandler()
 
# Note, the original GeoPackage is opened with both ogr and gdal.
# TODO, it might not be necessary actually
ogrDS = ogr.Open('/wrk/ekkylli/mtk/data/vektori/ogiir/data/MTK-geopackage-test-18-06-07.gpkg')
gdalDS = gdal.OpenEx('/wrk/ekkylli/mtk/data/vektori/ogiir/data/MTK-geopackage-test-18-06-07.gpkg', gdal.OF_VECTOR)

# get a layer with GetLayer('layername'/layerindex)
for layer in ogrDS:
    
    # Generate the name for new file
    layerName = layer.GetName()
    outFile='/wrk/ekkylli/mtk/data/vektori/ogiir/data/layers/'+layerName+'.gpkg'
    
    # Remove output shapefile if it already exists
    outDriver = ogr.GetDriverByName('GPKG')
    if os.path.exists(outFile):
        outDriver.DeleteDataSource(outFile)   
        
    #Save file with gdal, only one layer per file
    ds1 = gdal.VectorTranslate(outFile, gdalDS, layers = [layerName] , format = 'GPKG') 
    #Important, this is the way to save the file!
    del ds1       