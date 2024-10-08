from matplotlib import pyplot

loan = {}
def get_loan_info():
    loan["principal"] = float(input("Enter the amount of $ to loan: "))
    loan["interest"] = float(input("Enter the interest rate: ")) / 100
    loan["monthly payment"] = float(input("Enter the monthly payment: "))
    loan["money paid"] = 0

def show_loan_info(loan, months):
    print(f"\n=====Loan Status After {months} Months=====")
    for key in loan:
        print(f"{key.title()}: {loan[key]}")

def collect_interest(loan):
    loan["principal"] += loan["principal"] * loan["interest"] / 12

def make_monthly_payment(loan):
    loan["principal"] -= loan["monthly payment"]
    if loan["principal"] >= 0:
        loan["money paid"] += loan["monthly payment"]
    elif loan["principal"] < 0:
        loan["money paid"] -= (loan["principal"] - loan["monthly payment"])
        loan["principal"] = 0
    loan["principal"] = round(loan["principal"], 2)

def summarize_loan(loan, month, principal):
    print("\n===Loan Summary===")
    print(f"Initial Loan Value: ${principal}")
    print(f"How many months needed to pay the loan off: {month}")
    print(f"Total Amount Spent: ${loan["money paid"]:.2f}")
    print(f"Amount Spent on Interest: ${loan["money paid"] - starting_principal:.2f}")

def create_graph(data, loan):
    input(str(data))
    x_values = []
    y_values = []

    for _ in data:
        x_values += [_[0]]
        y_values += [_[1]]

    pyplot.plot(x_values, y_values)
    pyplot.title(f"{100*loan["interest"]}% Interest With ${loan["monthly payment"]} Monthly Payment")
    pyplot.xlabel("Month")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()

print("Welcome to the Loan Calculator App!")
month = 0

try:
    get_loan_info()
except ValueError:
    print("Invalid values given.")
    raise SystemExit
starting_principal = loan["principal"]
data_to_plot = [(0, loan["principal"])]

show_loan_info(loan, 0)
input("Press ENTER to begin paying off your loan. ")
while loan["principal"] > 0:
    if loan["principal"] > starting_principal:
        break

    month += 1
    collect_interest(loan)
    make_monthly_payment(loan)
    data_to_plot += [(month, loan["principal"])]
    show_loan_info(loan, month)

    if loan["principal"] == 0:
        break

if loan["principal"] == 0:
    summarize_loan(loan, month, starting_principal)
    create_graph(data_to_plot, loan)
else:
    print("\nYour loan will never be paid off.")
    print("You will never get ahead of your interest >:(")