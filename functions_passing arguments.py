#functions and passing arguments video 121

mySentence = " loves the color "

color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name): #name is the parameter
    lst = []
    for i in color_list: #i is for index/each individual element
        msg = "{0}{1}{2}".format(name,mySentence,i) #will use the name, the sentence and then i(index). Building 5 different sentences is an Array
        lst.append(msg)
    return lst


    

lst = color_function('Sally') #call the function. Sally is the argument
for i in lst: #i is for each individual element
    print(i)
    
