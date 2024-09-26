# Make sure that even the longest numbers can be shown (integers only)
import sys
sys.set_int_max_str_digits(0)

# ANSI formatting to be used throughout the program
# This makes the output look nicer.
bold = "\033[1m"
underline = "\033[4m"
end = "\033[0m"

def add(a, b):
    # Add numbers and return the sum
    sum = round(a + b, 4)
    print(f"The sum of {bold}{a}{end} and {bold}{b}{end} is {bold}{sum}{end}.")
    return f"{a} + {b} = {sum}"

def subtract(a, b):
    # Subtract numbers and return the difference
    diff = round(a - b, 4)
    print(f"The difference of {bold}{a}{end} and {bold}{b}{end} is {bold}{diff}{end}.")
    return f"{a} - {b} = {diff}"

def multiply(a, b):
    # Multiply numbers and return the product
    product = round(a * b, 4)
    print(f"The product of {bold}{a}{end} and {bold}{b}{end} is {bold}{product}{end}.")
    return f"{a} * {b} = {product}"

def divide(a, b):
    # Divide numbers and return the quotient
    # If the user divides by zero, return DIV ERROR
    if b != 0:
        quotient = round(a / b, 4)
        print(f"The quotient of {bold}{a}{end} and {bold}{b}{end} is {bold}{quotient}{end}.")
        return f"{a} / {b} = {quotient}"
    else:
        print("You cannot divide by zero.")
        return "DIV ERROR"

def exponent(a, b):
    # Raise a to the power of b and return the answer
    product = round(a ** b, 4)
    print(f"{bold}{a}{end} raised to the power of {bold}{b}{end} is {bold}{product}{end}.")
    return f"{a} ** {b} = {product}"

# Print welcome message
print(f"{bold}Welcome to the Calculator App!{end}")
print("Enter two numbers and an operation and the desired operation will be performed.")

history = []
while True:
    try:
        # Get numbers from the user
        print("")
        num1 = input("Enter a number: ")
        num2 = input("Enter another number: ")
        if "." in num1 or "." in num2:
            num1, num2 = float(num1), float(num2)
        else:
            num1, num2 = int(num1), int(num2)

        # Get operation from the user
        operation = input("Enter an operation (addition, subtraction, multiplication, division, or exponentation): ").lower().strip()

        # Perform calculations and save the result to history
        if operation in ["addition", "a"]:
            history += [add(num1, num2)]
        elif operation in ["subtraction", "s"]:
            history += [subtract(num1, num2)]
        elif operation in ["multiplication", "m"]:
            history += [multiply(num1, num2)]
        elif operation in ["division", "d"]:
            history += [divide(num1, num2)]
        elif operation in ["exponentation", "e"]:
            history += [exponent(num1, num2)]
        else:
            print("This operation doesn't exist.")
            history += ["OP ERROR"]
    except OverflowError:
        print("Result is too large to display.")
        history += ["OVERFLOW ERROR"]
    except ValueError:
        print("Invalid numbers. ")

    # Check if the user would like to do another calculation
    if not input("Would you like to do another calculation (y/n)? ").lower().startswith("y"):
        print(f"\n{underline}Calculation Summary:{end}")
        for _ in history:
            print(_)
        if len(history) == 0:
            print("No calculations saved")
        raise SystemExit