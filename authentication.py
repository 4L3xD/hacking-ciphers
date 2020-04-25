# Authentication

db = []

id = len(db) 
user_name = ''
password = ''

user = (id, user_name, password)

again = True

def hello_world():
    print('='*60 + '\n{:-^60}'.format('Authentica'))
    joke = input('\nHello! Do you want to joke of criptograph? y/n\n')
    # try:
    #     if joke != 'y' or joke != 'n':
    #         print('Enter a valid answer! (y or n)')
    # except ValueError:
    #     print('Ops! Something wrong is not right!')

    if joke == 'y':
        print('Let\'s go!\n')
        start()
    elif joke == 'n':
        print('See you later!\n')

def start():
    is_first = input('That\'s your first time here? y/n\n')
    # try:
    #     if is_first != 'y' or is_first != 'n':  
    #         print('Enter a valid answer! (y or n)') 
    # except ValueError:  
    #     print('Ops! Something wrong is not right!') 

    if is_first == 'y':
        first = True
    elif is_first == 'n':
        first = False

    if first == True:
        signUp()

        first = False
        
    if first == False:
        signIn()

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

def signUp():    
    user_exists = True
    while user_exists == True:
        user_name = input('\nSign up! Type your user name: ')

        user_exists = False
        for i in range(len(db)):
            if user_name == db[i][1]:
                user_exists = True
                print('User already exists!')
                print('Please, enter a valid name.')
                break
    print('Registered name!\nNow let\'s set a password for your security!')

    password = input('Enter your password: ')
    db.insert(len(db), (id+1, user_name, password))

def signIn():
    print('\nSign in!')
    user_acess = False
    password_acess = False

    while user_acess == False: 
        user_name = input('Type your user name: ')
        for i in range(len(db)):
            if user_name == db[i][1]:
                user_acess = True

                while password_acess == False:
                    password = input('Enter your password:')
                    if password == db[i][2]:
                        password_acess = True
                        welcome()                    
                    if password_acess == False:
                        print('Incorrect password!\n')
                break
        if user_acess != True:
            print('\nUser not found!\n')
    
def welcome():
    print('\nWelcome!\n')
    continue_program()

hello_world()
authentication()