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

import drill121_main
import drill121_func


def load_gui(self):
    # txt boxes
    self.txt_browse1 = tk.Entry(self.master,text='')
    self.txt_browse1.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(35,45),pady=(30,0),sticky=E)
    self.txt_browse2 = tk.Entry(self.master,text='')
    self.txt_browse2.grid(row=2,column=1,rowspan=1,columnspan=3,padx=(35,45),pady=(12,0),sticky=N+E+W)

    self.lbl_blank1 = tk.Label(self.master,text='')
    self.lbl_blank1.grid(row=3,column=2,padx=(35,45),pady=(12,0),sticky=E)
    self.lbl_blank2 = tk.Label(self.master,text='')
    self.lbl_blank2.grid(row=3,column=3,padx=(35,45),pady=(12,0),sticky=E)
    self.lbl_blank3 = tk.Label(self.master,text='')
    self.lbl_blank3.grid(row=3,column=4,padx=(35,45),pady=(12,0),sticky=E)
    self.lbl_blank4 = tk.Label(self.master,text='')
    self.lbl_blank4.grid(row=3,column=4,padx=(35,45),pady=(12,0),sticky=E)

    # btns
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse1.grid(row=1,column=0,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=2,column=0,padx=(15,0),pady=(10,0),sticky=W)
    self.btn_checkForFiles = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_checkForFiles.grid(row=3,column=0,padx=(15,0),pady=(10,0),sticky=W)
    self.btn_checkForFiles = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: drill121_func.ask_quit(self))
    self.btn_checkForFiles.grid(row=3,column=4,columnspan=1,padx=(15,0),pady=(10,0),sticky=E)



if __name__ == "__main__":
    pass
