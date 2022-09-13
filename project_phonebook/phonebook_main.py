



from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Import other modules so we have access to them
import phonebook_gui
import phonebook_func


# Frame is the Tkinter frame class that our own class will inherit from. ParentWindow = self/Frame = master
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master # self refers to the ParentWindow. Master refers to Frame.
        self.master.minsize(500,300) # height, width
        self.master.maxsize(500,300)

        # This CenterWindow method will center the app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title('The Tkinter Phonebook Demo')
        self.master.configure(bg='#F0F0F0') #bg=background color

        # This protocol method is a Tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))

        # Load in the GUI widgets from a separate module
        phonebook_gui.load_gui(self)

        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', underline=1, accelerator='Ctrl+Q', command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label='File', underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) #defines the particular drop down column and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label='How to Use This Program')
        helpmenu.add_separator()
        helpmenu.add_command(label='About This Phonebook Demo') # add_command is a child menubar item of the add_cascade parent item
        menubar.add_cascade(label='Help', menu=helpmenu) # add_cascade is a parent menubar item (visible heading)

        """
        Finally, we apply the config method of the widget to display the menu
        From here we could also pass in additional aprams for additional
        functionality or appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')
        
"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
