#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Phonebook Demo. Demonstrating OOP,
#           Tkinter GUI module, using Tkinter Parent and Child relationships.
#


from tkinter import *
import tkinter as tk

# these are our imported methods
import phonebook_gui
import phonebook_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame): # Frame is the primary Tkinter object (comes from Tkinter?)
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master # we invoked master from tkinter with Frame
        self.master.minsize(500,300) #(height,width)
        self.master.maxsize(500,300)
        #This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300) # calling from our import, self is passed in as a key
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self)) # miscrosoft's code for the red x in corner with an exit program catch
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)
        
        # Instantiate the TKinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="CTRL+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu) # defines the particular drop down column and tearoff=0 means do not separate from menubar
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebok Demo") # add_cascade is a parent menubar item (visible heading)
        menubar.add_cascade(label="Help", menu=helpmenu)
        '''
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional
            functionality or appearances such as a borderwidth.
        '''
        self.master.config(menu=menubar, borderwidth='1')



if __name__ == "__main__":
    root = tk.Tk() #syntax to create a Tkinter window
    App = ParentWindow(root) # our class with the Tkinter window attached via root
    root.mainloop() # to keep the app running, persistent
