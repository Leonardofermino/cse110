friends = []

new_friend = ""

while new_friend != "end":
    new_friend = input("Enter a friend's name (or 'end' to finish): ")
    if new_friend != "end":
        friends.append(new_friend)

if len(friends) >= 1:
    print("Your friends are:", end=" ")
    for i in range(len(friends)):
        if i == len(friends) - 1:
            print(f"and {friends[i]}.")
        elif i == len(friends) - 2:
            print(f"{friends[i]} ", end="")
        else:
            print(f"{friends[i]},", end=" ")
else:
    print("You have no friends.")