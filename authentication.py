# Authentication

db = []

id = len(db) 
user_name = ''
password = ''

user = (id, user_name, password)

def hello_world():
    print('='*60 + '\n{:-^60}'.format('Authentica'))
    joke = input('\nHello! Do you want to joke of criptograph? y/n\n').strip().lower()[0]
    while joke not in 'YyNn':
        joke = input('\nInvalid data! Do you want to joke of criptograph? y/n\n').strip().lower()[0]       
    if joke in 'Ss':
        print('\nLet\'s go!\n')
        start()
    if joke in 'Nn':
        print('\nSee you later!\n')
        exit()
    # try:
    #     if joke != 'y' or joke != 'n':
    #         print('Enter a valid answer! (y or n)')
    # except ValueError:
    #     print('Ops! Something wrong is not right!')

def start():
    is_first = input('That\'s your first time here? y/n\n')
    while is_first not in 'YyNn':
        is_first = input('Please, input y (for yes) or n (for no).\n')
    if is_first in 'Yy':
        first = True
    elif is_first in 'Nn':
        first = False

    if first == True:
        signUp()
        first = False
    if first == False:
        signIn()
    # try:
    #     if is_first != 'y' or is_first != 'n':  
    #         print('Enter a valid answer! (y or n)') 
    # except ValueError:  
    #     print('Ops! Something wrong is not right!') 

def authentication():
        start()
        signUp()
        signIn()

def continue_program():
    answer = input('\nContinue (y/n)?\n')
    # try:
    #     if answer != 'y' or answer != 'n':  
    #         print('Enter a valid answer! (y or n)') 
    # except ValueError:  
    #     print('Ops! Something wrong is not right!') 
    
    if answer =='y':
        authentication()
    else:
        exit()

def signUp():
    user_exists = True

    while user_exists == True:
        user_exists = False
        user_name = input('\nSign up! Type your user name: ')

        for i in range(len(db)):
            if user_name == db[i][1]:
                user_exists = True
                print('\nUser already exists!')
                print('\nPlease, enter a valid name.')
                break
    print('\nRegistered name!\n\nNow let\'s set a password for your security!')

    password = input('Enter your password: ')
    db.insert(len(db), (id+1, user_name, password))

def signIn():
    user_access = False
    password_access = False
    attempts_userName = 0
    attempts_password = 0
    
    print('\nSign in!')

    while user_access == False: 
        user_name = input('Type your user name: ')

        for i in range(len(db)):
            if user_name == db[i][1]:
                user_access = True

                while password_access == False:
                    password = input('Enter your password:')
                    if password == db[i][2]:
                        password_access = True
                        welcome()                    
                    if password_access == False:
                        print('\nIncorrect password!\n')
                        attempts_password += 1 
                        if attempts_password == 3:
                            print('\nDid you forget your password?!\n')
                break
        if user_access != True:
            print('\nUser not found!\n')
            attempts_userName += 1

            if attempts_userName == 3:
                print('\nattempts limit exceeded!\n')
                signUp()
    
def welcome():
    print('\nWelcome!\n')
    continue_program()

hello_world()
authentication()