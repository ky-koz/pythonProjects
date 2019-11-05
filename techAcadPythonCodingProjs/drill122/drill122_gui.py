#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Drill 122, For this drill,
#           you will need to write a script that creates a GUI with a button widget
#           and a text widget. Your script will also include a function that when it
#           is called will invoke a dialog modal which will allow users with the
#           ability to select a folder directory from their system. Finally, your
#           script will show the user’s selected directory path into the text field.
#
#
#           - Python 3 and the Tkinter module
#           - askdirectory() method from the Tkinter module
#           - a function linked to the button widget so that once the button
#           has been clicked will take the user’s selected file path retained
#           by the askdirectory() method and print it within your GUI’s text widget.
#
#



from tkinter import *
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
import sqlite3
import os

import drill122_func
import drill122_main


def load_gui(self):
    # txt boxes
    self.txt_browse1 = tk.Entry(self.master, text='')#command=lambda: drill122_func.getDir(self)) # was previously text=''
    self.txt_browse1.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(35,45),pady=(30,0),sticky=E)
    

    # btns
    self.btn_browse= tk.Button(self.master,width=12,height=1,text='Browse Files', command=lambda: drill122_func.getDir(self))
    # this will be used to invoke a function that pops up a module that then returns the input to the text box
    self.btn_browse.grid(row=1,column=0,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_checkForFiles = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: drill122_func.ask_quit(self))
    self.btn_checkForFiles.grid(row=3,column=4,columnspan=1,padx=(15,0),pady=(10,0),sticky=E)


    

if __name__ == "__main__":
    pass
