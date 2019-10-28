#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Drill from pg 103
#
# Instructions:
##Your script will need to use Python 3 and the sqlite3 module.
##
##Your database will require 2 fields, an auto-increment primary
##integer field and a field with the data type of string.
##
##Your script will need to read from the supplied list of file names
##at the bottom of this page and determine only the files from the list
##which ends with a “.txt” file extension.
##
##Next, your script should add those file names from the list ending
##with “.txt” file extension within your database.
##
##Finally, your script should legibly print the qualifying text files to the console.


import os
import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

def fileDir():
    conn = sqlite3.connect('drill103.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT \
            )")
        conn.commit()
    print("Text files from drill103.db: \n")
    cur = conn.cursor()
    for i in fileList:
        if i.endswith(".txt"):
            cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)",(i,))
            conn.commit()
            print(i)
    conn.close()

if __name__ == "__main__":
    fileDir()
