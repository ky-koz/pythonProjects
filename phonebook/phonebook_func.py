#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, Phonebook Demo. Demonstrating OOP,
#           Tkinter GUI module, using Tkinter Parent and Child relationships.
#


import os
from tkinter import *
import tkinter as tk
import sqlite3


import phonebook_main
import phonebook_gui


def center_window(self, w, h): # pass in the tkinter fram(master) reference and the w and h
    # get the user's screen width amd height
    screen_width = self.master.winfo_screenwidth() # naming it screen_width
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user clicks on the windows upper-right 'X' to ensure they want to close
def ask_quite(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"): # tkinter messagebox: window {title/name}{message}
        # this closes app
        self.master.destroy()
        os._exit(0) # program releases memory; os defined method


#===============================================================

def create_db(self): # name it create_db and pass in self
    conn = sqlite3.connect('db_phonebook.db') # connect and then create this db
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        # You must commit() to save changes and close the db connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    # data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com') ### This is in the video but not in the code
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor() # cur becomes an sqlite3 reference
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname, \
                    col_fullname,col_phone, col_email) VALUES (?,?,?,?,?)""", \
                    ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com'))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""") # passing the sqlite cursor fn
    count = cur.fetchone()[0] # extract the data from the cur command
    return cur,count

#Select item in ListBox
def onSelect(self,event):
    # calling the event is the self.lstList1 widget
    varList = event.widget # whatever is triggering the event
    select = varList.curselection()[0] # the index of our selection
    value = varList.get(select) # get the text of the index number
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor() #sqlite3 cursor object
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email \
            FROM tbl_phonebook WHERE col_fullname = (?)""", [value]) # only if matches the f/lname from the value(list)
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            # accessing different parts of the tuple that is returned
            self.txt_fname.delete(0,END) # delete the text box to clear it
            self.txt_fname.insert(0,data[0]) # insert the new info into the empty box
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])


def addToList(self):
    # these are built-in functions
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_fname = var_fname.strip() # remove any blank spaces before or after the user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title() # create capital letter at beginning of word
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # format we want in our listbox, will combine and normalize name into a fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
    if (len(var_fname) > 0 ) and (len(var_lname) > 0 ) and (len(var_phone) > 0) and(len(var_email) > 0): # enforces user to provide both names
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            # check the db for existence of the fullname, if so, we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook \
                    WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname, \
                    col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname, \
                    var_phone,var_email))
                self.lstList1.insert(END, var_fullname) # update into list box
                onClear(self) # automate clearing all text boxes at once
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please \
                    choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit() # save data in db
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")

def onDelete(self): # to delete something in the database
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value: get the listbox1's cursor selection
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the db... cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1: # is >1 then we know there are more than one user in the db
            confirm = messagebox.askokcancel("Delete Confirmation","All information associated with, \
                ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?" \
                .format(var_select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(varselect))
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
                # onRefresh(self) # update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database \
            and cannot be deleted at this time. \n\nPlease add another first before you can delete ({})." \
            .format(var_select,var_select))
    conn.close


def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    # onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

def onRefresh(self):
    # (re)Populate the listbox, coinciding with the db
    self.lstList1.delete(0,END) # delete everything in the listbox
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count: # this is a control, if you do more loops than the count you will produce an error
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""") # fullname is the value we put in our listbox
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item)) # take the item from the list and put it in the listbox
                i = i + 1
    conn.close()


def onUpdate(self): # to update info or make changes
    try:
        var_select = sef.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select)# list selecion's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling \
            the Update request.")
        return # go back and return to normal fn
    # the user will only be allowed to update changes for phone and emails.
    # for name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain db integrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): # ensure that there is data present
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user;s changes are already in
            # the db... ,meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = curfetchone()[0] # where we're getting the return value back
            print(count2)
            if count == 0 or count2 == 0: # if proposed changes are not already in the db, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}). \
                    \n\nProceed with the update request?".format(var_phone,var_email,var_value))
                print(response)
                if response: # if the user responds with okay then proceed with conn
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE \
                            col_fullname = '{2}'""".format(var_phone,var_email,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database \
                    for \n\nYour update request request has been cancelled.".format(var_phone, var_email))
            onClear(self) # clear the textbox
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit \
            the phone or email information.")
    onClear(self)


if __name__ == "__main__":
    pass # don't run anything, just pass
                














    
