from matplotlib import pyplot

def get_loan_info():
    # Get info from the user, making sure they don't enter negative values
    loan = {}

    loan["principal"] = abs(float(input("Enter the amount of $ to loan: ")))
    loan["interest"] = abs(float(input("Enter the interest rate: ")) / 100)
    loan["monthly payment"] = abs(float(input("Enter the monthly payment: ")))
    loan["money paid"] = 0

    return loan

def show_loan_info(loan, months):
    # Show the loan status after [months] months
    print(f"\n=====Loan Status After {months} Months=====")
    for key in loan:
        print(f"{key.title()}: {loan[key]}")

def collect_interest(loan):
    # Add interest to the loan, according to the current principal
    loan["principal"] += loan["principal"] * loan["interest"] / 12

def make_monthly_payment(loan):
    # Make the monthly payment and account for incomplete payments if needed
    loan["principal"] -= loan["monthly payment"]
    if loan["principal"] >= 0:
        loan["money paid"] += loan["monthly payment"]
    if loan["principal"] < 0:
        loan["money paid"] += (loan["monthly payment"] + loan["principal"])
        loan["principal"] = 0
    loan["principal"] = round(loan["principal"], 2)

def summarize_loan(loan, month, principal):
    # Summarize the loan
    print("\n===Loan Summary===")
    print(f"Initial Loan Value: ${principal}")
    print(f"How many months needed to pay the loan off: {month}")
    print(f"Total Amount Spent: ${loan["money paid"]:.2f}")
    print(f"Amount Spent on Interest: ${loan["money paid"] - principal:.2f}")

def create_graph(data, loan):
    # Create a graph of the loan data
    x_values = []
    y_values = []

    # Set the x/y values of the graph based on the data provided
    for _ in data:
        x_values += [_[0]]
        y_values += [_[1]]

    # Create the graph
    pyplot.plot(x_values, y_values)
    pyplot.title(f"{100*loan["interest"]}% Interest With ${loan["monthly payment"]} Monthly Payment")
    pyplot.xlabel("Month")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()

print("Welcome to the Loan Calculator App!")
month = 0

# Handles invalid inputs
try:
    loan = get_loan_info()
except ValueError:
    print("Invalid value(s) given.")
    raise SystemExit
starting_principal = loan["principal"]
data_to_plot = [(0, loan["principal"])]

show_loan_info(loan, 0)
input("Press ENTER to begin paying off your loan. ")
while loan["principal"] > 0:
    # If you can't pay off the loan, break the loop
    if loan["principal"] > starting_principal:
        break

    # Simulate paying interest, making monthly payments, and append data to data_to_plot
    month += 1
    collect_interest(loan)
    make_monthly_payment(loan)
    data_to_plot += [(month, loan["principal"])]
    show_loan_info(loan, month)

    # YOU FINALLY PAID OFF YOUR LOAN (unlike some)!!!
    if loan["principal"] == 0:
        break

# If you can pay off your loan, congrats!
# Otherwise, we'll automatically know that you should not take on this loan.
if loan["principal"] == 0:
    summarize_loan(loan, month, starting_principal)
    create_graph(data_to_plot, loan)
else:
    print("\nYour loan will never be paid off.")
    print("You will never get ahead of your interest >:(")
