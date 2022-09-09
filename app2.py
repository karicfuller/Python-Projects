
import app

def print_app2(): #function
    name = (__name__)
    return name


if __name__ == '__main__':
    #the above is calling code from within this script
    print('I am running code from {}'.format(print_app2()))

    #the following is calling code from imported dunder_methods
    print('I am running code from {}'.format(app.print_app()))

