
import sqlite3

conn = sqlite3.connect('assign.db') #connect to db

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assign( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT, \
        col_type TEXT \
        )") #create columns
    conn.commit()
conn.close()


conn = sqlite3.connect('assign.db') #connect to db

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_assign(col_file, col_type) VALUES(?,?)", \
                ('information.docx', '.docx'))#insert column info
    cur.execute("INSERT INTO tbl_assign(col_file, col_type) VALUES(?,?)", \
                ('Hello.txt', '.txt'))#insert column info
    cur.execute("INSERT INTO tbl_assign(col_file, col_type) VALUES(?,?)", \
                ('myImage.png', '.png'))#insert column info
    cur.execute("INSERT INTO tbl_assign(col_file, col_type) VALUES(?,?)", \
                ('myMovie.mpg', '.mpg'))#insert column info
    cur.execute("INSERT INTO tbl_assign(col_file, col_type) VALUES(?,?)", \
                ('World.txt', '.txt'))#insert column info
    cur.execute("INSERT INTO tbl_assign(col_file, col_type) VALUES(?,?)", \
                ('data.pdf', '.pdf'))#insert column info
    cur.execute("INSERT INTO tbl_assign(col_file, col_type) VALUES(?,?)", \
                ('myPhoto.jpg', '.jpg'))#insert column info
    conn.commit()
conn.close()


conn = sqlite3.connect('assign.db') #connect to db

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file FROM tbl_assign WHERE col_file = '*txt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item[0])
        print(msg)
    

    
