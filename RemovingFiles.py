import datetime
import os

rootdir = os.getcwd
print(rootdir)

for subdir , dirs and files in os.walk(rootdir):
    for file in files:
        filestatus = os.stat(file) 
        print(file)
        print('last access date     :'),
        print(datetime.datetime.fromtimestamp(filestatus.st_atime)),
        print('last modified date     :'),
        print(datetime.datetime.fromtimestamp(filestatus.st_mtime)),
        if datetime.datetime.fromtimestamp(filestatus.st_mtime) < datetime.datetime(2020,19,9):
            os.remove(file)
            print('Files Deleted Succesfully!')
        

    

