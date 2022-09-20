

import tkinter as tk
from tkinter import *
import webbrowser
import os


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title('Web Page Generator')

        # label above entry field
        self.lbl = Label(text='Enter custom text or click the Default HTML page button') 
        self.lbl.grid(row=0, column=0, padx=(20), pady=(20,0))

        # entry field
        self.enter_info = Entry(self.master) 
        self.enter_info.grid(row=1, column=0, columnspan=3, padx=(30,15), pady=(10,10), sticky=W+E)  

        # default button
        self.default_btn = Button(self.master, text='Default HTML Page', width=20, height=1, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=1, padx=(0,10), pady=(0,10))

        # submit button
        self.submit_btn = Button(self.master, text='Submit Custom Text', width=20, height=1, command=self.entryHTML)
        self.submit_btn.grid(row=2, column=2, padx=(0,10), pady=(0,10))


    def defaultHTML(self):
        htmlText = 'You Couldn\'t Think of Anything to Type Inside the Box?' # verbiage if default button is clicked
        htmlFile = open('index.html', 'w') # w=write only
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</h1>\n</body>\n</html>'
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.get().open_new_tab('file:///' + os.getcwd() + '/index.html')

    def entryHTML(self):
        htmlText = self.enter_info.get() # verbiage entered into field
        htmlFile = open('index.html', 'w') 
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</h1>\n</body>\n</html>'
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.get().open_new_tab('file:///' + os.getcwd() + '/index.html')
                      
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

