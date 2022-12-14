



# phonebook_main


from tkinter import *
import tkinter as tk
from tkinter import messagebox

import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from. ParentWindow = self Frame = master
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs): # once you define your class, you reference it with "main"/master refers to Frame
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master # self refers to the ParentWindow. Master refers to Frame. 
        self.master.minsize(500,300) #height,width
        self.master.maxsize(500,300)
        
        # This CenterWindow method will center the app on the user's screen
        phonebook_func.center_window(self,500,300) # on any Windows computer box will be center of screen
        self.master.title('The Tkinter Phonebook Demo')
        self.master.configure(bg='#F0F0F0') #bg=background
            
        # This protocol method is a tkinger built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))

        # Load in the GUI widgets from a separate module
        phonebook_gui.load_gui(self)


if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

##############################################

# phonebook_gui


from tkinter import *
import tkinter as tk

        
# Import other modules
import phonebook_main
import phonebook_func

    
def load_gui(self):
        
    self.lbl_fname = tk.Label(self.master,text='First Name:') # define the class(Label) to create the object
    self.lbl_fname = grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W) # place the object
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname = grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone:')
    self.lbl_phone = grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_user = tk.Label(self.master,text='User:')
    self.lbl_lname = grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.txt_fname = tk.Entry(self.master, text = '')
    self.txt_fname.grid(row=1, column=0, rowspan=1, coulumnspan=2, padx=(30,40), pady=(0,0), sticky=N+W)
    self.txt_lname = tk.Entry(self.master, text = '')
    self.txt_lname.grid(row=3, column=0, rowspan=1, coulumnspan=2, padx=(30,40), pady=(0,0), sticky=N+W)
    self.txt_phone = tk.Entry(self.master, text = '')
    self.txt_phone.grid(row=5, column=0, rowspan=1, coulumnspan=2, padx=(30,40), pady=(0,0), sticky=N+W)
    self.txt_email = tk.Entry(self.master, text = '')
    self.txt_email.grid(row=7, column=0, rowspan=1, coulumnspan=2, padx=(30,40), pady=(0,0), sticky=N+W)

    # Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0, yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: phonebook_func.onSelect(self,event)) #event listener(bind)that waits for an event 
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+E+S+W)

    self.btn_add = tk.Button(self.master, width=12, height=2, text='Add', command=lambda: phonebook_func.addToList(self))
    self.btn_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky=W)
    self.btn_update = tk.Button(self.master, width=12, height=2, text='Update', command=lambda: phonebook_func.onUpdate(self))
    self.btn_update.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky=W)
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete', command=lambda: phonebook_func.onDelete(self))
    self.btn_add.grid(row=8, column=2, padx=(25,0), pady=(45,10), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close', command=lambda: phonebook_func.ask_quit(self))
    self.btn_close.grid(row=8, column=4, columnspan=1, padx=(15,0), pady=(45,10), sticky=E)

    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)


if __name__=="__main__":
    pass


#######################################

# phonebook_func

import os
from tkinter import *
import tkinter as tk
import sqlite3

# import other modules
import phonebook_main
import phonebook_gui

def center_window(self, w, h): #pass in the tkinter Frame(master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth() # reports what the users screen height and width is
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the use's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# Catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
        # this closes the app
        self.master.destroy()
        os._exit(0) #releases memory from user's system

########################################
        # CREATE DATABASE
        
def create_db(self):
    conn = sqlite3.connect('db_phonebook.db') # will create db if it doesn't exist
    with conn: # with the connection, do the following:
        cur = conn.cursor() # cursor required to do SQL queries
        cur.execute('CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );')
        # You must commit() to save changes and close the database connection
        conn.commit()
    conn.close()
    first_run(self)

##########################################

def first_run(self):
    Data = ('John', 'Doe', '111-111-1111', 'jdoe@email.com')
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe', '111-111-1111', 'jdoe@email.com'))
            conn.commit()
    conn.close()

def count_records(cur): # (cur) allows you to use SQL queries
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count

# Select item in ListBox
def onSelect(self,event): # onSelect from gui module - when ListboxSelect is clicked
    # calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

        def addToList(self):
            var_fname = self.txt_fname.get()
            var_lname = self.txt_lname.get()
            # normalize the data to keep it consistent in the database
            var_fname = var_fname.strip() # This will remove any blank spaces before and after the user's entry
            var_lname = var_lname.strip() # .strip will ensure that the first character in teach word is capitalized
            var_fname = var_fname.title() # .title will ensure first letter is capitalized
            var_lname = var_lname.title()
            var_fullname = ('{} {}'.format(var_fname, var_lname,)) # combine our normalized names into a fullname
            print('var_fullname: {}'.format(var_fullname))
            var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: # will use this soon
        print("Incorrect Email Format!!!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and(len(var_email) > 0): # enforce the user to provide both names
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))#,(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")
        

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
######             onRefresh(self) # update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()


def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##    onRefresh(self) # update the listbox of the changes
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
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only be alowed to update changes for phone and emails.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): # ensure that there is data present
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0] # count = phone #
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0] # count2 = email address
            print(count2)
            if count == 0 or count2 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_value))
                print(response)
                if response:
                    #conn = sqlite3.connect('db_phonebook.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone,var_email,var_value))
                        onClear(self) # clears out text boxes
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)



if __name__ == "__main__":
    pass


            



    



    
        
        
        
        















        
