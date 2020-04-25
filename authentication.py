# Authentication
import pyperclip

user_db = []
lenght_user_db = int(len(user_db))

password_db = []
lenght_password_db = int(len(password_db))

def authentication():
    again = False

    print('='*60 + '\n{:-^60}'.format('Authentica'))
    print('\nHello! Do you want to joke of criptograph? Y/n')
    joke = input()
    if joke == 'y':
        print('Let\'s go!\n')
        again = True
    else:
        print('See you later!')

    while again == True:

        print('That\'s your first time here? Y/n')
        is_first = input()
        if is_first == 'y':
            first = True
        elif is_first == 'n':
            first = False

        if first == True:
            print('\nSign up! Type your user name: ')
            user = input()
            user_db.insert(lenght_user_db+1, user)
            print('Enter your password: ')
            password = input()
            password_db.insert(lenght_password_db+1, password)

            first = False
            signIn()

        else:
            signIn()

        print('Continue (y/N)?')
        answer = input()
        if answer == 'n':
            again = False
        elif answer =='y':
            again = True

def signIn():
    print('\nSign in!')
    user = input('Type your user name: ')
    for user_name in range(len(user_db)):
        if user == user_db[user_name]:
            user_acess = True
        else:
            print('User not found!')
    if user_acess == True:
        print('Enter your password:')
        password = input()
        for user_password in range(len(password_db)):
            if password == password_db[user_password]:
                password_acess = True
                welcome()                    
        if password_acess == False:
            print('Incorrect password!')

def welcome():
    print('Welcome!')

authentication()