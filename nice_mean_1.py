

def start():
    f_name = 'Kari'
    l_name = 'Fuller'
    age = 46
    gender = 'Female'
    get_info(f_name,l_name,age,gender)



def get_info(f_name,l_name,age,gender):
    name = input('What is your name? ')
    print('My name is {} {}. I am a {} year old {}.'.format(f_name,l_name,age,gender))
    








if __name__ == '__main__':
    start()
