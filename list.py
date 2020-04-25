db = [0, 1, 2]
user_id = 3

for i in range(len(db)):
    if db[i] == user_id:
        print('Usuário já existe!')
        new_user = False
    else:
        new_user = True
if new_user == True:
    db.insert(len(db)+1, user_id)
    print('Usuário inserido!')

print(db)
