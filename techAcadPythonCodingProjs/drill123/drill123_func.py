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

def fileDir(self):
    conn = sqlite3.connect('drill123.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fname TEXT, \
                    col_mtime TEXT \
                    )")
        conn.commit()
    conn.close()

def getDirSource(self):
    btnSource = fileDialog.askdirectory()
    self.txt_sourceDir.insert(INSERT,btnSource)

def getDirDest(self):
    btnDest = fileDialog.askdirectory()
    self.txt_destDir.insert(INSERT,btnDest)


def transfer(self):
    source = self.txt_sourceDir.get()
    destination = self.txt_destDir.get()
    sourceList = os.listdir(source)
    fileDir(self)
    for files in sourceList:
        if files.endswith(".txt"):
            abPath_src = os.path.join(source, files)
            abPath_dest = os.path.join(destination, files)
            mod_time = os.path.getmtime(abPath_src)
            print("{} {}".format(files, mod_time))
            shutil.move(abPath_src, abPath_dest)
            conn = sqlite3.connect('drill123.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_fname, col_mtime) VALUES (?, ?)", (files, mod_time,))
                conn.commit()
            conn.close()





if __name__ == "__main__":
    pass
