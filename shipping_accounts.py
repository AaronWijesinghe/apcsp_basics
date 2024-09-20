# List of accounts
users = ["aaronw", "americac", "vincentg", "josephf", "zhu"]

# Display welcome message and get username
print("Welcome to the Shipping Accounts Portal!")
username = input("\nHi, what is your username? ").lower()

if username in users:
    # Show shipping prices
    print(f"\nWelcome back to your account, {username}!")
    print("These are the current shipping prices:")
    print("")
    print("Shipping 0-99 items: $5.10/ea")
    print("Shipping 100-499 items: $5.00/ea")
    print("Shipping 500-999 items: $4.95/ea")
    print("Shipping 1,000+ items: $4.80/ea")
    print("")

    # Get number of orders from the user
    # If the order string is numeric, continue with the program
    items = input("How many items do you want to ship? ")
    if items.isnumeric():
        items = int(items)

        # Depending on the amount of orders, display the correct prices
        if items == 0:
            input("You must ship more than 0 items. ")
            raise SystemExit
        elif 0 < items <= 99:
            print(f"To ship {items} items, it will cost you ${items*5.10:.2f} at $5.10 per item.")
        elif 100 <= items <= 499:
            print(f"To ship {items} items, it will cost you ${items*5.00:.2f} at $5.00 per item.")
        elif 500 <= items <= 999:
            print(f"To ship {items} items, it will cost you ${items*4.95:.2f} at $4.95 per item.")
        else:
            print(f"To ship {items} items, it will cost you ${items*4.80:.2f} at $4.80 per item.")

        # Confirm or cancel the order
        if input("\nWould you like to place this order (y/n)? ").lower().startswith("y"):
            input(f"Alright, your order of {items} items has been placed! ")
        else:
            input("Your order has been canceled. ")
    else:
        input("Invalid amount of orders. ")
else:
    # If the username is invalid, display the goodbye message
    input("Sorry, you don't have an account with us. ")