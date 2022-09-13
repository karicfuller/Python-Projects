


from abc import ABC, abstractmethod #import abstractmethod data from abc module

class Money(ABC): 
    def allowance(self,amount):
        print('Your allowance for this week is: ',amount)
    @abstractmethod #information on data not provided
    def deposit(self,amount):
        pass

class paymentType(Money): #uses info from parent class
    def deposit(self,amount): 
        print('Your allowance in the amount of ${} was deposited to your bank. '.format(amount))

money = paymentType()
money.allowance('$50')
money.deposit('50')
