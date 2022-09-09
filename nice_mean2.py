

def start(nice=0, mean=0, name=''):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player
        for playing again and continue with game
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != '':
        print('\nThank you for playing again, {}!'.format(name))
        else:
            stop = True
            while stop: #while stop == True(same thing)
                if name == '':
                    name = input('\nWhat is your name? \n>>>).capitalize()
                    if name != '':
                        print('\nWelcome, {}!'.format(name))
                        print('\nIn this game, you will be greeted \nby several different people. \nYou can chose to be nice or mean')
                        print('but at the end of the game your fate \nwill be sealed by your actions.')
                        stop = False #stopping block of code
        return name

def nice_mean(nice=0,mean=0,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a \nconverstation. Will you be nice \nor mean? (N/M) \n>>>: ').lower()#makes n/m lowercase
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice = (nice + 1) #0+1
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()

        







if __name__ == '__main__':
    start()
