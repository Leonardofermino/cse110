"""
Author: Leonardo Fermino

Purpose: Create a word puzzle game



"""
from random import randint

list_secret = ['mosiah', 'nephi', 'jesus', 'lehi', 'temple', 'faith', 'hope', 'charity', 'love', 'service', 'obedience', 'repentance', 'baptism', 'sacrament', 'prayer', 'scripture', 'prophet', 'apostle', 'bishop', 'ward', 'stake', 'zion']

# secret_word = list_secret[randint(0, len(list_secret) - 1)]
secret_word = 'mosiah'

print("Welcome to the word guessing game!\n")

puzzle = ''
guess_count = 0

while puzzle != secret_word:
    puzzle = input('Your hint is: ')
    guess_count += 1
    if puzzle != secret_word:
        print('Your guess was not correct.')
print(f'Congratulations! You guessed it!\nIt only took you {guess_count} attempts.')