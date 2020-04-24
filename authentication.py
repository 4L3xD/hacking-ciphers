# Authentication
import pyperclip

user_db = []
password_db = []

def authentication():

    again = True

    print('That\'s your first time here?')
    not_is_first = input()
    if not_is_first.find == 'no':
        first = False
    elif not_is_first == 'yes':
        first = True

    while again == True: 

        if first == True:
            lenght_db = int(len(user_db))

            print('\nSign up! Type your user name: ')
            user = input()
            user_db.insert(lenght_db+1, user)
            print('Enter your password: ')
            password = input()
            password_db.insert(lenght_db+1, password)

            first = False
            
        elif first == False:
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

    print('Continue (y/N)?')
    answer = input()
    if answer == 'n' or 'N':
        again = False


def welcome():
    print('Welcome!')

authentication()