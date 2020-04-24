# import pyperclip

print('Enter your name: ', end='')
name = input()

randomElem = 0
while int(randomElem) < 6:
    print('Enter the random number for encrypt: ')
    randomElem = input()

    try:
        if int(randomElem) < 6:
            print('Your secret is not protected. \nTry again! ')
    except ValueError:
        print('Oh shit! \nSomething went wrong. Restart the program!')

print('Type a secret in numbers, {}: '.format(name), end='')
# pyperclip.copy(input())
# print(pyperclip.paste())
secret = [int(x) for x in input()]
# secret = []
# for x in input():
#     secret.append(int(x))

def encrypt():
    for i in range (len(secret)):
        exp = pow(int(secret[i]), int(randomElem))
        secret[i] = exp**(1/2)

encrypt()
print('Your secret has been encrypted: {}.'.format(secret))