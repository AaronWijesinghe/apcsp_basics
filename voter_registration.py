# ANSI formatting to be used throughout the program
# This makes the output look nicer.
bold = "\033[1m"
underline = "\033[4m"
end = "\033[0m"

# Display welcome message
print(f"{bold}Welcome to the Voter Registration App!{end}")

# Ask for name/age and set list of parties
name = input("\nPlease enter your name: ").title()
age = input(f"Please enter your age {bold}(MUST be 18+){end}: ")
parties = ["republican", "democratic", "independent", "libertarian", "green"]

# If the user's age isn't a number, exit
if not age.isnumeric():
    print("\nYou age must be a number.")
    raise SystemExit
else:
    age = int(age)

if age >= 18:
    # If age is over 18, display parties and congratulate the user
    print(f"\nCongratulations {name}! You are old enough to register to vote.")
    print(f"\n{underline}Here is a list of political parties to join:{end}")
    for _ in parties:
        print(f"\t• {_.title()}")

    # Ask user what party they want to vote for
    party = input("\nWhat party would you like to join? ").lower()
    if party in parties:
        print("")
        print(f"Congratulations {name}! You have joined the {party.title()} party!")
    else:
        print(f"{name}, this party does not exist.")
        raise SystemExit

    # Check if the party is major/minor/independent
    if party in ["republican", "democratic"]:
        print("That is a major party!")
    elif party in ["libertarian", "green"]:
        print("That is not a major party.")
    else:
        print("You are an independent person!")

else:
    # If the user is under 18 years old, exit the program
    print(f"\nYou are not old enough to vote. {bold}You must be 18+ to vote.{end}")