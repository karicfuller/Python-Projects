
import tkinter
from tkinter import *



#create tkinter window
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='darkgray')

        self.varFName = StringVar()
        self.varLName = StringVar()
        self.varFName.set('Bob')
        self.varLName.set('Smith')

        print(self.varFName.get())
        print(self.varLName.get())

        self.txtFName = Entry(self.master,text=self.varFName, font = ('Helvetica', 16), fg='black', bg='lightblue')
        self.txtFName.pack() #makes text box

        self.txtLName = Entry(self.master,text=self.varLName, font = ('Helvetica', 16), fg='black', bg='lightblue')
        self.txtLName.pack()





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #without will launch and then close
