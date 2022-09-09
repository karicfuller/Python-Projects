Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')
listofAnimals = list(animal)
print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox']
listofAnimals.append("honey badger")
print (listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox', 'honey badger']
myString = "Hello! I am pleased to meet you"
newString = list(myString)
print(newString)
['H', 'e', 'l', 'l', 'o', '!', ' ', 'I', ' ', 'a', 'm', ' ', 'p', 'l', 'e', 'a', 's', 'e', 'd', ' ', 't', 'o', ' ', 'm', 'e', 'e', 't', ' ', 'y', 'o', 'u']
newString = myString.split(" ")
print(newString)
['Hello!', 'I', 'am', 'pleased', 'to', 'meet', 'you']

thisList = ["apple", "banana", "cherry"]
print(thisList)
['apple', 'banana', 'cherry']
myset= {"apple", "banana", "cherry"}
print(myset)
{'banana', 'apple', 'cherry'}
{'banana', 'apple', 'cherry'}
{'banana', 'apple', 'cherry'}
myset.add("orange")
print(myset)
{'banana', 'apple', 'cherry', 'orange'}
myset.remove("banana")
print(myset)
{'apple', 'cherry', 'orange'}

    myset= {"apple", "banana", "cherry"}
    
SyntaxError: unexpected indent

dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'Phone': '123-456-7890'},
             'em_5678': {'fname': 'Mary', 'lname': 'Jones', 'Phone': '805-704-9693'} }
print(dic_users[emp5678])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(dic_users[emp5678])
NameError: name 'emp5678' is not defined
print(dic_sers[emp_5678])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(dic_sers[emp_5678])
NameError: name 'dic_sers' is not defined. Did you mean: 'dic_users'?
print(dic_users[emp_5678])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(dic_users[emp_5678])
NameError: name 'emp_5678' is not defined
print(dic_users[em5678])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(dic_users[em5678])
NameError: name 'em5678' is not defined
print(dic_users[em_5678])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(dic_users[em_5678])
NameError: name 'em_5678' is not defined
print(dic_users['em_5678'])
{'fname': 'Mary', 'lname': 'Jones', 'Phone': '805-704-9693'}
print(dic_users['em_1234']['Phone'])
123-456-7890
print('User: {} {}\nPhone: {}'.format(dic_users['em_1234']['fname'], dic_users['em_5678']['lname'], dic_users['em_5678']['Phone']))
User: Bob Jones
Phone: 805-704-9693





























thisDict = {
    "fname": "Oscar",
    "lname": "Prado",
    "Phone": "708-9896"
    }
print(thisDict)
{'fname': 'Oscar', 'lname': 'Prado', 'Phone': '708-9896'}
