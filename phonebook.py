



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


    
        
        
        
        















        
