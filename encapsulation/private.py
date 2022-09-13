

#private variable
class Colors: 
    def __init__(self):
        self.__firstColor = 'red' #setting first color to red
        
    def getPrivate(self):
        print(self.__firstColor)

    def setPrivate(self, private): #setting as private
        self.__firstColor = private
        
objPrivate = Colors()
objPrivate.getPrivate()
objPrivate.setPrivate('blue') #changing color to blue
objPrivate.getPrivate()


