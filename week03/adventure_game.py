"""
Author: Leonardo Fermino

Purpose: Create a text-based game using if-else statements

"""

print("Welcome to the Adventure Game!")
print("You find yourself in a dark forest. You hear strange noises around you.")
print("Do you want to EXPLORE the forest, FOLLOW the path, or RETURN to the village?")

choice1 = input("Your choice: ").strip().lower()

if choice1 == "explore":
    print("\nYou decide to explore the forest. As you wander deeper, you find a mysterious cave.")
    print("Do you ENTER the cave or CONTINUE exploring?")
    
    choice2 = input("Your choice: ").strip().lower()
    
    if choice2 == "enter":
        print("\nInside the cave, you find a treasure chest. But there's also a sleeping dragon!")
        print("Do you OPEN the chest, SNEAK past the dragon, or LEAVE the cave?")
        
        choice3 = input("Your choice: ").strip().lower()
        
        if choice3 == "open":
            print("\nThe dragon wakes up and chases you out of the cave! You barely escape with your life.")
        elif choice3 == "sneak":
            print("\nYou successfully sneak past the dragon and find a hidden exit. You escape with a bag of gold!")
        elif choice3 == "leave":
            print("\nYou leave the cave safely, but you can't help but wonder what was inside the chest.")
        else:
            print("\nInvalid choice. The dragon wakes up and you run for your life!")
    
    elif choice2 == "continue":
        print("\nYou continue exploring the forest and find a beautiful clearing with a sparkling pond.")
        print("Do you DRINK from the pond or REST by the pond?")
        
        choice3 = input("Your choice: ").strip().lower()
        
        if choice3 == "drink":
            print("\nThe water is magical! You feel rejuvenated and gain the strength to continue your journey.")
        elif choice3 == "rest":
            print("\nAs you rest, you fall asleep and wake up to find yourself back at the edge of the forest.")
        else:
            print("\nInvalid choice. You wander aimlessly and eventually find your way back to the village.")
    
    else:
        print("\nInvalid choice. You get lost in the forest and eventually find your way back to the village.")

elif choice1 == "follow":
    print("\nYou follow the path and come across a fork in the road.")
    print("Do you go LEFT towards the mountains or RIGHT towards the river?")
    
    choice2 = input("Your choice: ").strip().lower()
    
    if choice2 == "left":
        print("\nYou head towards the mountains and find an abandoned cabin.")
        print("Do you ENTER the cabin or CONTINUE up the mountain?")
        
        choice3 = input("Your choice: ").strip().lower()
        
        if choice3 == "enter":
            print("\nInside the cabin, you find supplies and a map that helps you on your journey.")
        elif choice3 == "continue":
            print("\nYou climb the mountain and discover a breathtaking view. You feel accomplished!")
        else:
            print("\nInvalid choice. You lose your way and end up back at the fork in the road.")
    
    elif choice2 == "right":
        print("\nYou head towards the river and find a small boat.")
        print("Do you TAKE the boat or FOLLOW the riverbank?")
        
        choice3 = input("Your choice: ").strip().lower()
        
        if choice3 == "take":
            print("\nYou take the boat and sail down the river, discovering a hidden village.")
        elif choice3 == "follow":
            print("\nYou follow the riverbank and find a bridge that leads to a bustling town.")
        else:
            print("\nInvalid choice. You wander aimlessly and eventually return to the fork in the road.")
    
    else:
        print("\nInvalid choice. You get lost and eventually find your way back to the starting point.")

elif choice1 == "return":
    print("\nYou return to the village and decide to rest. Maybe you'll try again another day.")

else:
    print("\nInvalid choice. You stand frozen in indecision and the adventure ends before it begins.")
