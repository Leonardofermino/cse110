import random
play = "yes"

start = 1
finish = 50

while play == "yes":
    number = random.randint(start,finish)

    pick = int(input(f"Please guess a number between {start} and {finish}: "))

    guess_qty = 1

    while pick != number:
        if pick > number:
            print("The number you chose is too high.")
        elif pick < number:
            print("The number you picked is too low.")
        pick = int(input(f"Try again. Please guess a number between {start} and {finish}: "))
        guess_qty += 1
        

    print(f"You guessed the correct number. The number was {number}.")
    print()

    if guess_qty == 1:
        print(f"It took you {guess_qty} guess to guess this number.")
    else:
        print(f"It took you {guess_qty} guesses to guess this number.")

    play = input("Would you like to play again? Yes or No? ")
    play = play.lower()