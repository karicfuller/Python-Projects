
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
        self.master.config(bg='lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.lblFName = Label(self.master,text='First Name: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))#makes grid/x=horizontal, y=vertical

        self.lblLName = Label(self.master,text='Last Name: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))#makes grid

        self.txtFName = Entry(self.master,text=self.varFName, font = ('Helvetica', 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1,padx=(30,0), pady=(30,0)) #makes grid

        self.txtLName = Entry(self.master,text=self.varLName, font = ('Helvetica', 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1,padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text='Submit', width = 10, height=2)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE)





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #without will launch and then close
