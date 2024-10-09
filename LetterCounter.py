# Print welcome message
print("Welcome to the Letter Counter App!")

# Ask for the user's name and state the program's purpose
name = input("\nWhat is your name? ").title()
print(f"\nHello {name}!")
print("I will count the number of times that a specific letter occurs in a message.")

# Get the message and letter to scan for, standardizing it in the process
message = input("\nPlease enter a message: ").lower()
letter = input("Enter a letter to scan for: ").lower()

# Show how many letters are in the provided message
letter_count = message.count(letter)
print(f"\n{name}, your message has {letter_count} {letter}{"'s" if letter_count > 1 or letter_count == 0 else ""} in it.")
