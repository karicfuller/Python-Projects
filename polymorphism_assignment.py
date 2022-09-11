
#parent class
class Automobile: 
    make = 'Honda'
    model = 'CR-V'

    def autoInfo(self):
        entry_make = input('Enter the make of your automobile: ')
        entry_model = input('Enter the model of your automobile: ')
        if (entry_make == self.make):
            print('I have a Honda too!')
        else:
            print('That is a cool car!')
        
#child class A_Car
class A_Car:
    cost = 10.00
    doors = 4

    def carInfo(self):
        entry_make = input('Enter the make of your car: ')
        entry_doors = input('How many doors does your car have: ')
        if (entry_doors == self.doors):
            print('My car has 4 doors too!')
        else:
            print('Oh, my car has 4 doors!')

#child class A_Truck
class A_Truck:
    year = 2019
    doors = 2

    def truckInfo(self):
        entry_make = input('Enter the make of your truck: ')
        entry_doors = input('How many doors does your truck have: ')
        if (entry_year == self.year):
            print('Mine is a 2019 too!')
        else:
            print('Oh, mine is a 2019!')
        


auto = Automobile()
auto.autoInfo()

car = A_Car()
car.carInfo()
        
truck = A_Truck()
truck.truckInfo()

