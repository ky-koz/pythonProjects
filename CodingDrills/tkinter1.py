import tkinter
from tkinter import * 



class ParentWindow(Frame):
    def __init__ (self, master): #init is preprogrammed in, arguments **args and keyword arguments **kwargs
        Frame.__init__ (self)

        self.master = master # master is being passed into the contianer self.master, primary screen that will pop up
        self.master.resizable(width=True, height=True) # True makes resizable, False disables resize
        self.master.geometry('{}x{}'.format(700, 400)) # giving it a specific size in pixels
        self.master.title('Learning Tkinter!')
        self.master.config(bg='darkgray') # can also refer to color as a hex

        self.varFName = StringVar() #to create a tkinter variable
        self.varLName = StringVar()


        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.lblFName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=1, column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue') # paint the textbox, self.master is the full window
        self.txtFName.grid(row=0, column=1,padx=(30,0), pady=(30,0)) # diff geometry/placement  managers are used to paint on forms or windows

        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1,padx=(30,0), pady=(30,0)) # if you don't include a colspan, it is set at default 1

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit) # command gives the button a purpose
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE) #NE is short for North East

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self): # it is a part of the self class so you have to pass that through
        fn = self.varFName.get() #
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self): # we want this command to close the window
        self.master.destroy()
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()






























if __name__ == "__main__":
    root = Tk() #named Tkinter root
    App = ParentWindow(root) # attaching ParentWindow to root and passing it to App
    root.mainloop() # .mainloop keeps an app continuously run until the user shuts it down
