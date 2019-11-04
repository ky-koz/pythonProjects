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
root = tk.Tk()

import main
import func


def load_gui(self):

    # btns
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Button 1')
    self.btn_browse1.grid(row=0,column=0,columnspan=2,padx=(15,0),pady=(30,0),sticky=E)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Button 2')
    self.btn_browse2.grid(row=1,column=0,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse3 = tk.Button(self.master,width=12,height=1,text='Button 3')
    self.btn_browse3.grid(row=2,column=0,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse4 = tk.Button(self.master,width=12,height=1,text='Button 4')
    self.btn_browse4.grid(row=3,column=0,padx=(15,0),pady=(30,0),sticky=W)

    self.btn_browse6 = tk.Button(self.master,width=12,height=1,text='Button 6')
    self.btn_browse6.grid(row=1,column=1,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse7 = tk.Button(self.master,width=12,height=1,text='Button 7')
    self.btn_browse7.grid(row=2,column=1,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse8 = tk.Button(self.master,width=12,height=1,text='Button 8')
    self.btn_browse8.grid(row=3,column=1,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse9 = tk.Button(self.master,width=12,height=1,text='Button 9')
    self.btn_browse9.grid(row=0,column=2,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Button 10')
    self.btn_browse2.grid(row=1,column=2,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse3 = tk.Button(self.master,width=12,height=1,text='Button 11')
    self.btn_browse3.grid(row=2,column=2,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse4 = tk.Button(self.master,width=12,height=1,text='Button 12')
    self.btn_browse4.grid(row=3,column=2,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse5 = tk.Button(self.master,width=12,height=1,text='Button 13')
    self.btn_browse5.grid(row=0,column=3,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse6 = tk.Button(self.master,width=12,height=1,text='Button 14')
    self.btn_browse6.grid(row=1,column=3,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse7 = tk.Button(self.master,width=12,height=1,text='Button 15')
    self.btn_browse7.grid(row=2,column=3,padx=(15,0),pady=(30,0),sticky=W)
    self.btn_browse8 = tk.Button(self.master,width=12,height=1,text='Button 16')
    self.btn_browse8.grid(row=3,column=3,padx=(15,0),pady=(30,0),sticky=W)

    root.grid_columnconfiguration(3, minsize=100)
if __name__ == "__main__":
    pass
