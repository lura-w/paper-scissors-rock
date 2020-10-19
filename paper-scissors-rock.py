import random as rd

execution = True

while execution == True:
    elements = ['paper', 'rock', 'scissors']
    user = input('Option: ')
    if user == 'exit':
        execution = False
        continue
    elif user not in elements:
        print(' Wrong name')
        continue
    cp = elements[rd.randint(0,2)]
    if user == cp:
        print(f' {user} tie')
    elif (user == elements[0] and cp == elements[1]) or (user == elements[2] and cp == elements[0]) or (user == elements[1] and cp == elements[2]):
        print(f' User wins with {user} to cp using {cp}')
    else:
        print(f' Cp wins using {cp} to user with {user}')
    if user == 'exit':
        execution = False