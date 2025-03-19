# Description: This program asks the user for a name, adjectives, nouns, verbs, and adverbs to create a story like Mad Libs. I used a function to determine whether to use "a" or "an" based on the first letter of the adjective. The program then prints the story with the user's input.

def get_article(word):
    if word[0].lower() in 'aeiou':
        return 'an'
    else:
        return 'a'

name = input("Enter a name: ").capitalize()
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb ending in -ing: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb ending in -ing: ")
adverb = input("Enter an adverb: ")
adjective3 = input("Enter one more adjective: ")

print(f"Once upon a time, there was {get_article(adjective1)} {adjective1} person named {name}. One day, {name} was {verb1} {get_article(adjective1)} {noun1} when suddenly {get_article(adjective2)} {adjective2} {noun2} appeared! The {noun2} started {verb2} {adverb}, which made {name} feel very {adjective3}.")