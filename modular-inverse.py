simbols = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'
key = input('Choose you key: ')

for modular_inverse in range(len(simbols)):
    if (int(key) * modular_inverse)%int(len(simbols)) == 1:
        print('{} is the modular inverse of {} mod {}, because ({}*{})%{} = 1'
        .format(modular_inverse, key, len(simbols), key, modular_inverse, len(simbols)))
    