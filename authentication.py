# Authentication
import pyperclip

user_db = []
password_db = []

def authentication():
    print('That\'s your first time here?')
    first = True

    if first == True:
        lenght_db = int(len(user_db))

        print('\nSign up! Type your user name: ')
        user = input()
        user_db.insert(lenght_db+1, user)
        print('Enter your password: ')
        password = input()
        password_db.insert(lenght_db+1, password)

        first = False
    else:
        print('\nSign in!')
        user_name = input('Type your user name: ')
        for userName in range(len(user_db)):
            if user_name == user_db[userName]:
                print('Enter your password:')
                user_password = input()
                if user_password != password:
                    print('Incorrect password!')
                else:
                    welcome()                    
        else:
            print('User not found!')

def welcome():
    print('Welcome!')

authentication()