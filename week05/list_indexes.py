items = []
item = ""

while item != "end":
    item = input("Please enter the items of the shopping list (type: quit to finish): ")
    if item != "end":
        items.append(item)

print("\nThe shopping list is: ")
for item in items:
    print(f"Item: {item}")

print("\nThe shopping list with indexes is: ")
for item in items:
    print(f"{items.index(item)}: {item}")

index = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")
items[index] = new_item

print("\n\nThe new shopping list with indexes is: ")
for item in items:
    print(f"{items.index(item)}: {item}")
