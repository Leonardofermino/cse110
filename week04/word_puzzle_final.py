"""
Author: Leonardo Fermino

Purpose: Create a word puzzle game

added: I added a list of words to be used as the secret word. The program will randomly select one of the words from the list.

"""
from random import randint

list_secret = ['mosiah', 'nephi', 'jesus', 'lehi', 'temple', 'faith', 'hope', 'charity', 'love', 'service', 'obedience', 'repentance', 'baptism', 'sacrament', 'prayer', 'scripture', 'prophet', 'apostle', 'bishop', 'ward', 'stake', 'zion']

secret_word = list_secret[randint(0, len(list_secret) - 1)]

print("Welcome to the word puzzle game!")

puzzle = ''
guess_count = 0

while True:
    print('\nYour hint is: ', end='')

    if puzzle == '':
        print('_ ' * len(secret_word))
    else:
        for i in range(len(secret_word)):
            if puzzle[i] == '_':
                print('_', end=' ')
            else:
                print(puzzle[i], end=' ')
    
    guess = input('\nWhat is your guess? ').strip().lower()
    guess_count += 1

    if len(guess) != len(secret_word):
        print(f"Your guess must be {len(secret_word)} letters long. Try again.")
        continue

    if guess == secret_word:
        print(f"\nCongratulations! You guessed it!\nIt only took you {guess_count} attempts.")
        break

    puzzle = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            puzzle += guess[i].upper()
        elif guess[i] in secret_word:
            puzzle += guess[i].lower()
        else:
            puzzle += '_'