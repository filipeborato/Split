from zipfile import ZipFile
import os
from os.path import basename

# Zip the files from given directory that matches the filter
def zipFilesInDir(dirName, zipFileName, filter):
   # Ensure the output directory exists
   os.makedirs(os.path.dirname(zipFileName), exist_ok=True)
   
   # create a ZipFile object
   with ZipFile(zipFileName, 'w') as zipObj:
       # Iterate over all the files in directory
       for folderName, subfolders, filenames in os.walk(dirName):
           for filename in filenames:
               if filter(filename):
                   # create complete filepath of file in directory
                   filePath = os.path.join(folderName, filename)
                   # Add file to zip
                   zipObj.write(filePath, basename(filePath))
