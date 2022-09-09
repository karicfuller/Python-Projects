
import dunder_methods

def print_dunder_methods2(): #function
    name = (__name__)
    return name


if __name__ == '__main__':
    #the above is calling code from within this script

    #the following is calling code from imported dunder_methods
    print('I am running code from {}'.format(print_dunder_methods.print_dunder_methods()))

