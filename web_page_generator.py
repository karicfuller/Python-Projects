



import tkinter as tk
from tkinter import *
import webbrowser
import os




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        print("Hello")
        htmlText = "Stay Tuned for Our Amazing Summer Sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        #webbrowser.open_new_tab("index.html")

        webbrowser.get().open_new_tab('file:///' + os.getcwd() + '/index.html')









        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

