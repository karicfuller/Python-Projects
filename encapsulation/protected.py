

#protected variable
class Numbers: 
    def __init__(self):
        self._firstNumber = 7 #setting first color to red
        
        
objProtected = Numbers()
objProtected._firstNumber = 17
print(objProtected._firstNumber)
