# extra: created a table to show the cart aligned and included the individual and total price of each item

"""
Author: Leonardo Fermino
Purpose: milestone shopping cart project
"""

cart_items = []
cart_prices = []
cart_quantities = []

print("Welcome to the Shopping Cart Program!")

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    choice = input("Please enter an action: ")

    match choice:
        case "1":
            item = input("What item would you like to add? ")
            price = float(input(f"What is the price of '{item}'? $"))
            quantity = int(input(f"How many of '{item}'? "))
            cart_items.append(item)
            cart_prices.append(price)
            cart_quantities.append(quantity)
            print(f"'{quantity} {item}(s)' has been added to the cart.")
            
        case "2":
            if len(cart_items) == 0:
                print("The cart is empty.")
            else:
                header = (f"| {'Item No.':^8} | "
                         f"{'Item Name':<15} | "
                         f"{'Price':^8} | "
                         f"{'Quantity':^15} | "
                         f"{'Total Price':^15} |")
                print("\n" + header)
                print("-" * len(header))

                for i in range(len(cart_items)):
                    total_item_price = cart_prices[i] * cart_quantities[i]
                    print(f"| {i+1:^8} | "
                          f"{cart_items[i]:<15} | "
                          f"${cart_prices[i]:>7.2f} | "
                          f"{cart_quantities[i]:^15} | "
                          f"${total_item_price:>14.2f} |")
                    
        case "3":
            if len(cart_items) == 0:
                print("The cart is empty.")
            else:
                index = int(input("Which item would you like to remove? ")) - 1
                if 0 <= index < len(cart_items):
                    current_quantity = cart_quantities[index]
                    remove_quantity = int(input(f"How many {cart_items[index]}(s) would you like to remove? (Current: {current_quantity}): "))
                    
                    if remove_quantity >= current_quantity:
                        print(f"All '{cart_items[index]}' has been removed.")
                        cart_items.pop(index)
                        cart_prices.pop(index)
                        cart_quantities.pop(index)
                    else:
                        cart_quantities[index] -= remove_quantity
                        print(f"{remove_quantity} '{cart_items[index]}(s)' has been removed.")
                else:
                    print("Invalid item number.")
                    
        case "4":
            total = sum(cart_prices[i] * cart_quantities[i] for i in range(len(cart_items)))
            print(f"The total price of the items in the shopping cart is ${total:.2f}")
            
        case "5":
            print("Thank you. Goodbye.")
            break
            
        case _:
            print("Invalid choice. Please try again.")
