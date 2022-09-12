


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
class A_Car(Automobile):
    cost = 10.00
    doors = 4

    def autoInfo(self):
        entry_make = input('Enter the make of your car: ')
        entry_doors = input('How many doors does your car have: ') #replaceing model
        if (entry_doors == self.doors):
            print('My car has 4 doors too!')
        else:
            print('Oh, my car has 4 doors!')

#child class A_Truck
class A_Truck(Automobile):
    year = 2019
    doors = 2

    def autoInfo(self):
        entry_make = input('Enter the make of your truck: ')
        entry_year = input('What year is your truck: ') #replacing model with year
        if (entry_year == self.year):
            print('Mine is a 2019 too!')
        else:
            print('Oh, mine is a 2019!')
        


auto = Automobile()
auto.autoInfo()

car = A_Car()
car.autoInfo()
        
truck = A_Truck()
truck.autoInfo()

