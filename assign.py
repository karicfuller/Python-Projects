
import sqlite3

conn = sqlite3.connect('assign.db') 

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assign( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )") 
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('assign.db')

with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith('.txt'):
            print(file)
