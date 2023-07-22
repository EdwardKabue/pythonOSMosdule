import os
from datetime import datetime

#print current directory.
#print(os.getcwd())

#change directory
os.chdir("/home/code7/")
print(os.getcwd())

#list files and folders in the current directory.
#print(os.listdir())

#create directory and its sub-directory
#os.makedirs("testDir/SubtestDir")

#create single directory without sub-directory
#os.mkdir("testDir")

#delete directory recursively
#os.removedirs("testDir/SubtestDir")

#remove single directory
#os.rmdir("testDir/SubtestDir")

#renaming a file
#os.rename("python-handbook.pdf", "pythonHandbook.pdf")

#get file information
print(os.stat("pythonHandbook.pdf").st_size) #print size in bytes.

mod_time = os.stat("pythonHandbook.pdf").st_mtime #get file modification time stamp
print(datetime.fromtimestamp(mod_time)) #print file modification time stamp in human readable form.

