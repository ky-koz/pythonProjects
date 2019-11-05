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
from tkinter import messagebox
import tkinter.filedialog
import sqlite3
import os

import drill122_func
import drill122_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # master frame configuration
        self.master = master
        self.master.minsize(500,160)
        self.master.maxsize(500,160)

        # center window method
        drill122_func.center_window(self,500,200)
        self.master.title("Search Directory")
        self.master.configure(bg="#F0F0F0")

        # u.r.corner "x"
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill122_func.ask_quit(self))
        arg = self.master

        drill122_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk() #syntax to create a Tkinter window
    App = ParentWindow(root) # our class with the Tkinter window attached via root
    root.mainloop()
