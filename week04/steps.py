string = input('Enter a word: ')
favorite = input('What is your favorite letter? ')

for i in range(0, len(string)):
    if string[i] == favorite:
        print('_', end='')
    else:
        print(string[i].lower(), end='')