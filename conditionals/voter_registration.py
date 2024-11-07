import os
import json

# ANSI formatting to be used throughout the program
# This makes the output look nicer.
bold = "\033[1m"
underline = "\033[4m"
end = "\033[0m"

# Set predefined list of parties
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

# Load previously saved votes
if os.path.exists("votes.json"):
    try:
        votes = json.loads(open("votes.json").read())
    except:
        print("An error occured when parsing the votes.")
        os.remove("votes.json")
        raise SystemExit
else:
    votes = {
        "Republican": [],
        "Democratic": [],
        "Independent": [],
        "Libertarian": [],
        "Green": []
    }

# Display welcome message
print(f"{bold}Welcome to the Voter Registration App!{end}")

# Ask for name/age
name = input("\nPlease enter your full name: ").title().strip()
if len(name.split(" ")) < 2:
    print(f"You must enter your {bold}full name{end} to vote.")
    raise SystemExit
age = input(f"Please enter your age {bold}(MUST be 18+){end}: ")

# If the user's age isn't a number, exit
if not age.isnumeric():
    print(f"\nInvalid age. {bold}Your age must be a number.{end}")
    raise SystemExit
else:
    age = int(age)

# If the user already voted, exit the program
vote = {
    "name": name,
    "age": age
}
for _ in votes:
    if vote in votes[_]:
        print(f"\nYou can't vote again, {name}.\nChosen party: {_}")
        raise SystemExit

if age >= 18:
    # If age is over 18, display parties and congratulate the user
    print(f"\nCongratulations {name}! You are old enough to register to vote.")
    print(f"\n{underline}Here is a list of political parties to join:{end}")
    for _ in parties:
        print(f"\t• {_}")

    # Ask user what party they want to vote for
    chosen_party = input("\nWhat party would you like to join? ").title().strip()
    if chosen_party in parties:
        print("")
        print(f"Congratulations {name}! You have joined the {chosen_party} party!")
    else:
        print(f"{name}, this party does not exist. Please see the above parties.")
        raise SystemExit

    # Check if the party is major/minor/independent
    if chosen_party in ["Republican", "Democratic"]:
        print("That is a major party!")
    elif chosen_party in ["Libertarian", "Green"]:
        print("That is not a major party.")
    elif chosen_party == "Independent":
        print("You are an independent person!")

    # Save the vote to votes.json
    votes[chosen_party] += [vote]
    open("votes.json", "w").write(json.dumps(votes, indent=4))
else:
    # If the user is under 18 years old, exit the program
    print(f"\nYou are not old enough to vote. {bold}You must be 18+ to vote.{end}")
    if age == 17:
        print(f"You can vote in 1 year.")
    else:
        print(f"You can vote in {18 - age} years.")