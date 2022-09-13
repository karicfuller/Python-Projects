


from abc import ABC, abstractmethod #import abstractmethod data from abc module

class Money(ABC): 
    def allowance(self,amount):
        print('Your allowance for this week is: ',amount)
    @abstractmethod #information on data not provided
    def deposit(self,amount):
        pass

class paymentType(Money): 
    def deposit(self,amount): 
        print('Your allowance in the amount of ${} was deposited to your bank. '.format(amount))

#uses info from both classes
money = paymentType()
money.allowance('$50')
money.deposit('50')
