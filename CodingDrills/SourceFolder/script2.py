#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Drill from pg 100
#


import os
import time
# import the os module and the time module


fPath = 'C:\\Users\\Kyla Kozole\\Desktop\\Repositories\\pythonProjects\\drill100'

print("\nFiles and directories in folder Drill100\n",fPath,":")

dirList = os.listdir(fPath)
print(dirList)


def fileDir():
    print("\nFile names and mod times: \n")
    for i in dirList:
        if i.endswith(".txt"):
            mod_time = os.path.getmtime(i)
            abPath = os.path.join(fPath, i)
            print("{} {}".format(i, mod_time))
           



if __name__ == "__main__":
    fileDir()
