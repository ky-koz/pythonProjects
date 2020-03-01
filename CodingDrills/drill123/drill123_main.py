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

import drill123_func
import drill123_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # master frame configuration
        self.master = master
        self.master.minsize(555,280)
        # self.master.maxsize(500,160)

        # center window method
        drill123_func.center_window(self,555, 280)
        self.master.title("Search Directory")
        self.master.configure(bg="#F0F0F0")
        self.varSource = StringVar()
        self.varDest = StringVar()

        # u.r.corner "x"
        # self.master.protocol("WM_DELETE_WINDOW", lambda: drill122_func.ask_quit(self))
        # arg = self.master

        drill123_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk() #syntax to create a Tkinter window
    App = ParentWindow(root) # our class with the Tkinter window attached via root
    root.mainloop()

