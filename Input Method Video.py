Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
fName = "Daniel"
lName = "Christie"
print(fName + lName)
DanielChristie
print(fName + " " + lName)
Daniel Christie
print("Hello {} {}, welcome to Python!".format(fName,lName))
Hello Daniel Christie, welcome to Python!
fName = input("What is your first name?")
What is your first name?
fName = input("What is your first name?\n>>> ")
What is your first name?
>>> Daniel
fName = input("What is your \"first name\"?\n>>> ")
What is your "first name"?
>>> Daniel
fName = input("What is your 'first name'?\n>>> ")
What is your 'first name'?
>>> Daniel
fName
'Daniel'
lName = input("What is your last name?\n>>>)
              
SyntaxError: unterminated string literal (detected at line 1)
lName = input("What is your last name?"\n>>>)
              
SyntaxError: unexpected character after line continuation character
fName
              
'Daniel'
fName = input("What is your last name?\n>>> ")
              
What is your last name?
>>> Christie
print("Hello {} {}, welcome to Python!".format(fName,lName))
              
Hello Christie Christie, welcome to Python!
fName = input("What is your first name?\n>>> ")
              
What is your first name?
>>> Daniel
fName
              
'Daniel'
lName = input("What is your last name?\n>>> ")
              
What is your last name?
>>> Christie
lName
              
'Christie'
print("Hello {} {}, welcome to Python!".format(fName,lName))
              
Hello Daniel Christie, welcome to Python!
