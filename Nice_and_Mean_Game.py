

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
                name = input('\nWhat is your name? \n>>>').capitalize()
            if name != '':
                print('\nWelcome, {}!'.format(name))
                print('\nIn this game, you will be greeted \nby several different people. \nYou can chose to be nice or mean')
                print('but at the end of the game your fate \nwill be sealed by your actions.')
                stop = False #stopping block of code
                return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a \nconverstation. Will you be nice \nor mean? (N/M) \n>>>: ').lower()#makes n/m lowercase
        if pick == 'n':
            print('\nThe stranger walks away smiling like an idiot...')
            nice = (nice + 1) #0+1
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly, calls you an ass and storms off...')
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()


def show_score(nice,mean,name):
    print('\nYour current total: \n{}, nice) and ({}, mean)'.format(name,nice,mean))

        
def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    #substitute the {} wildcards with our variable values
    print('\nAwesome {}, you win! \nEveryone loves you! \nYou are my hero and I am now obsessed with \nyou and will stalk you for the rest of your life!'.format(name))
    #call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    #substitute the {} wildcards with our variable values
    print('\nAhhh {}, too bad, game over! \n{}, you are a loser and \na piece of crap!'.format(name))
    #call again function and pass in our variables
    again(nice,mean,name)

    
def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('\nAre we doing this again? (y/n):\n>>> ').lower()
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print('\nOh, so sad! Fine, get outta here then!')
            stop = False
            quit()
        else:
            print('\nEnter ( Y ) for YES, ( N ) for NO: \n>>> ') #will start loop again because never stopped


def reset(nice,mean,name):
    nice = 0 #resetting nice to default value
    mean = 0 #reseting mean to default value
    #notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)






if __name__ == '__main__':
    start()
