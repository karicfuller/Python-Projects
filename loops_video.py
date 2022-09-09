#Loops Video 123

mySentence = " loves the color "

color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name): #name is the parameter
    lst = []
    for i in color_list: #i is for index/each individual element
        msg = "{0}{1}{2}".format(name,mySentence,i) #will use the name, the sentence and then i(index). Building 5 different sentences is an Array
        lst.append(msg)
    return lst


    

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print("You need to provide your name!")
        elif name == 'Sally':
            print("Sally, you may not use this software.")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


get_name()
