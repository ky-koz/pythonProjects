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
import tkinter.filedialog
from tkinter import messagebox
import sqlite3
import os
import shutil

import drill123_func
import drill123_main


def load_gui(self):
    # lbls
    self.lbl_sourceDir = tk.Label(self.master, text='Choose Source Directory:')
    self.lbl_sourceDir.grid(row=0, column=0, padx=(35, 17), pady=(30, 0), sticky=W)
    self.lbl_destDir = tk.Label(self.master, text='Choose Desitination Directory:')
    self.lbl_destDir.grid(row=2, column=0, padx=(35, 20), pady=(10, 0), sticky=W)
    self.lbl_transfer = tk.Label(self.master, text='Transfer files ending in .txt from \n Start Directory to the Destination Directory')
    self.lbl_transfer.grid(row=4, column=0, padx=(35, 0), pady=(10, 0), sticky=W)

    # txt boxes
    self.txt_sourceDir = tk.Entry(self.master, text='', width="60")  # command=lambda: drill122_func.getDir(self)) # was previously text=''
    self.txt_sourceDir.grid(row=1, column=0, rowspan=1, columnspan=3, padx=(35, 8), pady=(5, 0), sticky=W)
    self.txt_destDir = tk.Entry(self.master, text='', width="60")  # command=lambda: drill122_func.getDir(self)) # was previously text=''
    self.txt_destDir.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(35, 8), pady=(5, 30), sticky=W)

    # btns
    self.btn_browseStart = tk.Button(self.master, width=12, height=1, text='Browse', command=lambda: drill123_func.getDirSource(self))
    self.btn_browseStart.grid(row=1, column=3, padx=(15, 0), pady=(10, 0), sticky=E)
    self.btn_browseDest = tk.Button(self.master, width=12, height=1, text='Browse', command=lambda: drill123_func.getDirDest(self))
    self.btn_browseDest.grid(row=3, column=3, padx=(15, 0), pady=(10, 30), sticky=E)
    self.btn_search = tk.Button(self.master, width=12, height=2, text='Transfer', command=lambda: drill123_func.transfer(self))
    self.btn_search.grid(row=4, column=2, padx=(15, 0), pady=(20, 0), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program', command=lambda: drill123_func.ask_quit(self))
    self.btn_close.grid(row=4, column=3, padx=(15, 0), pady=(20, 0), sticky=E)


if __name__ == "__main__":
    pass