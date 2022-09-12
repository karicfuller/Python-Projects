


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
