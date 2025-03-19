# I included whether the user consumed something extra and can enter the amount, whether they want to tip and the amount that each adult should pay of the total. In addition, I gave the option to choose the payment method and give a discount if it is in cash.
# I also included a loop to calculate the amount that each adult should pay and the option to pay in cash or credit card.



child = float(input("What is the price of a child's meal? ").replace(',', '.'))
adult = float(input("What is the price of an adult's meal? ").replace(',', '.'))

children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

subtotal = child * children + adult * adults
print(f"\nSubtotal: ${subtotal:.2f}")

# Perguntar se consumiram mais algo
additional_amount = float(input("\nDid you consume anything else? If yes, enter the amount, otherwise enter 0: ").replace(',', '.'))
if additional_amount > 0:
    subtotal += additional_amount
    print(f"\nSubtotal: ${subtotal:.2f}")

tax_rate = float(input("\nWhat is the sales tax rate? ").replace(',', '.'))
tax = subtotal * tax_rate / 100
print(f"Sales Tax: ${tax:.2f}")
total = subtotal + tax
print(f"\nSubtotal after taxes: ${total:.2f}")

# Perguntar quanto querem dar de gorjeta
tip = float(input("\nTip? If yes, enter the amount, otherwise enter 0:  ").replace(',', '.'))
total += tip

print(f"Total: ${total:.2f}")

# Dividir o valor total pelo número de adultos
if adults > 0:
    per_adult = total / adults
    print(f"Each adult should pay: ${per_adult:.2f}")

    adult_counter = 1
    while adults > 0:
        print(f"Adult {adult_counter} should pay: ${per_adult:.2f}")
        # Oferecer desconto de 5% se pagar em dinheiro
        payment_method = input("\nWill you pay in cash or credit card? (cash/credit): ").strip().lower()
        if payment_method == 'cash':
            discount = per_adult * 0.05
            cash = per_adult - discount
            print(f"Discount for paying in cash: ${discount:.2f}")
            print(f"Total after discount: ${cash:.2f}")
            payment = float(input("\nWhat is the payment amount? ").replace(',', '.'))
            change = payment - cash
            print(f"Change: ${change:.2f}\n")
        else:
            print("Swipe your credit card!!\n")
        adults -= 1
        adult_counter += 1
    
    print("Thank you for your visit!")

else:
    print("There are no adults to pay the bill. Call the police!!")