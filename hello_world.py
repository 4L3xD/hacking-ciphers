name = print(input('Hello world! \nWhat\'s your name? '))
print('Its is good to meet you, {}.\n'.format(name))

message = 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1
print(translated)