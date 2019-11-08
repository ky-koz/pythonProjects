#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Drill 123, For this drill,
#           provide the user with a graphical user interface that includes two buttons
#           allowing the user to browse their own system and select a source directory and a destination directory.
#
#           Your script should also show those selected directory paths in their own corresponding text fields.
#
#           Next, your script will need to provide a button for the user to execute a function that
#           should iterate through the source directory:
#           checking for the existence of any files that end with a “.txt” file extension and if so, cut the
#           qualifying files and paste them within the selected destination directory.
#
#           Finally, your script will need to record the file names that were moved and their corresponding
#           modified time-stamps into a database and print out those text files and their modified
#           time-stamps to the console.
#
#           - Python 3 and the Tkinter module
#           - listdir() method from the OS module to iterate through all files within a specific directory.
#           - path.join() method from the OS module to concatenate the file name to its file path, forming
#               an absolute path
#           - getmtime() method from the OS module to find out the latest date the file has been created or
#               last modified
#           - database to record the qualifying file and corresponding modified time-stamp
#           - print each file ending with a “.txt” file extension and its corresponding mtime to the console
#           - use the move() method from the Shutil module to cut all qualifying files and paste them
#               within the destination directory
#
#


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog
import sqlite3
import os
import shutil

import drill123_main
import drill123_gui

fileDialog = tkinter.filedialog

# Center tk window center of user's screen
def center_window(self, w, h):
    # get user's screen w x h
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calc x and y coords to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# to close the program
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # this closes app
        self.master.destroy()
        os._exit(0)


def getDirSource(self):
    btnSource = fileDialog.askdirectory()
    if btnSource:
        self.txt_sourceDir.insert(INSERT,btnSource)

def getDirDest(self):
    btnDest = fileDialog.askdirectory()
    if btnDest:
        self.txt_destDir.insert(INSERT,btnDest)


def transfer(self):
    source = self.varSource.get()
    destination = self.varDest.get()
    fPath = source
    for files in source:
        if files.endswith(".txt"):
            mod_time = os.path.getmtime(files)
            abPath = os.path.join(fPath, files)
            print("{} {}".format(files, mod_time))
            shutil.copy(files, destination)
            conn = sqlite3.connect('drill123.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?, ?)", (files, mod_time,))
            conn.commit()
        conn.close()

# direct copy from script103.py
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

def fileDir():
    conn = sqlite3.connect('drill123.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT \
            )")
        conn.commit()
    conn.close()
# end copy from script103.py

# direct copy of script2.py


print("\nFiles and directories in folder Drill100\n", fPath, ":")

dirList = os.listdir(fPath)
print(dirList)

def fileDir():
    print("\nFile names and mod times: \n")
    for i in dirList:
        if i.endswith(".txt"):
            mod_time = os.path.getmtime(i)
            abPath = os.path.join(fPath, i)
            print("{} {}".format(i, mod_time))
# end copy from script2.py

#copy from phonebook_func.py --> need to change this function to include the if .txt fn
#Select item in ListBox
def searchDir(self,event):
    # calling the event is the self.lstList1 widget
    varList = event.widget # whatever is triggering the event
    select = varList.curselection()[0] # the index of our selection
    value = varList.get(select) # get the text of the index number
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor() #sqlite3 cursor object
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email \
            FROM tbl_phonebook WHERE col_fullname = (?)""", [value]) # only if matches the f/lname from the value(list)
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            # accessing different parts of the tuple that is returned
            self.txt_fname.delete(0,END) # delete the text box to clear it
            self.txt_fname.insert(0,data[0]) # insert the new info into the empty box
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
# end copy of phonebook_func.py




if __name__ == "__main__":
    pass