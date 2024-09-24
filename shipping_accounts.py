# List of accounts
users = ["aaronw", "americac", "vincentg", "josephf", "mrzhu"]

# Display welcome message and get username
print("Welcome to the Shipping Accounts Portal!")
username = input("\nHi, what is your username? ").lower()

if username in users:
    # Show shipping prices
    print(f"\nWelcome back to your account, {username}!")
    print("These are the current shipping prices:")
    print("\n[Amount of Items]\t\t\t[Price]")
    print("Shipping 0-99 items:\t\t$5.10/item")
    print("Shipping 100-499 items:\t\t$5.00/item")
    print("Shipping 500-999 items:\t\t$4.95/item")
    print("Shipping 1,000+ items:\t\t$4.80/item")

    # Get number of orders from the user
    # If the order string is numeric, continue with the program
    items = input("\nHow many items do you want to ship? ")
    if items.isnumeric():
        items = int(items)

        # Depending on the amount of orders, set the correct cost per item
        if items == 0:
            print("You must order more than 0 items. ")
            raise SystemExit
        elif items < 100:
            cost = 5.10
        elif items < 500:
            cost = 5.00
        elif items < 1000:
            cost = 4.95
        else:
            cost = 4.80

        # Calculate and display bill
        bill = round(items * cost, 2)
        print(f"To ship {items} items, it will cost you ${bill:.2f} at ${cost:.2f} per item.")

        # Confirm or cancel the order
        if input("\nWould you like to place this order (y/n)? ").lower().startswith("y"):
            print(f"Alright, your order of {items} items has been placed! ")
        else:
            print("Your order has been canceled. ")
    else:
        print("Invalid amount of items. ")
else:
    # If the username is invalid, display the goodbye message
    print("Sorry, you don't have an account with us. ")