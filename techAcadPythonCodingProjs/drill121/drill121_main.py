#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Drill p 121
#

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import drill121_gui
import drill121_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # master frame configuration
        self.master = master
        self.master.minsize(500,160)
        self.master.maxsize(500,160)

        # center window method
        drill121_func.center_window(self,500,200)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        # u.r.corner "x"
        self.master.protocol("WM_DELETE_WINDOW", lambda: func.ask_quit(self))
        arg = self.master

        drill121_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
