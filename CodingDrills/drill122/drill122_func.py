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

# imports

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog
import sqlite3
import os

import drill122_main
import drill122_gui


fileDialog = tkinter.filedialog

def center_window(self, w, h):
    # get user's screen w x h
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calc x and y coords to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
'''
def getDir(self):
    varDir = fileDialog.askdirectory()
    varDir = StringVar(root)
    directoryName = StringVar()
    # print(varDir)
    self.get.insert(varDir)
   # return self.get()
   # directoryName.set(varDir)
'''
def getDir(self):
    varDir = fileDialog.askdirectory()
    if varDir:
        self.txt_browse1.insert(INSERT,varDir)

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # this closes app
        self.master.destroy()
        os._exit(0)





if __name__ == "__main__":
    pass
