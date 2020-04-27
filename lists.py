# Lists

users = {'user':{'name': '', 'age': 0},
    'gender':["feminine", "masculine", "fluid", "no binary", "queer", "other"],
    'ethnicity':['indigenous','black', 'white', 'other']
    }

print('Enter your information\n')
users['user'][0] = input('user name: ')
users['user'][1] = input('age: ')

print('\nType a number.')
print('1.feminine | 2.masculine | 3.fluid | 4.no binary | 5.queer | 6.other\n')
gender =  input('gender: ')
print('1.indigenous | 2.black | 3.white | 4.other\n')
ethnicity = input('ethnicity: ')

print('user: ', users['user'][0],',','age: ', users['user'][1],',',
    'gender: ', users['gender'][int(gender)-1],',',
    'ethnicity: ', users['ethnicity'][int(ethnicity)-1])

