#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Drill p 121
#

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

import gui
import main


def center_window(self, w, h):
    # get user's screen w x h
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calc x and y coords to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # this closes app
        self.master.destroy()
        os._exit(0)




if __name__ == "__main__":
    pass
