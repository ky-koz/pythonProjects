#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Drill from pg 100
#

"""
Your script will need to use Python 3
and the OS module.
"""
import os
import time


"""
Your script will need to use the path.join() method
from the OS module to concatenate the file name to
its file path, forming an absolute path.
"""
fName = 'doc01.txt'
fPath = 'C:\\Users\\Kyla Kozole\\Desktop\\Repositories\\pythonProjects\\drill100'

abPath = os.path.join(fPath, fName)
print(abPath)



"""
Your script will need to use the listdir() method
from the OS module to iterate through all files
within a specific directory.
"""
print("\nFiles and directories in folder Drill100\n",fPath,"' :")

dirList = os.listdir(fPath)
print(dirList)



"""
Your script will need to use the getmtime() method
from the OS module to find the latest date that each
text file has been created or modified.
"""

mod_time = os.path.getmtime(fPath)
print("\nLast modification time since the epoch:",mod_time)

local_time = time.ctime(mod_time)
print("Last modification time(Local time):",local_time)

print(os.path.basename(fPath))



"""
Your script will need to print each file ending
with a “.txt” file extension and its
corresponding mtime to the console.
"""
print("\nFiles that end in .txt from Drill100:")

txtList = 


