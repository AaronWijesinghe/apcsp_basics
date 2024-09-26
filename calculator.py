def add(a, b):
    # Add numbers and return the sum
    sum = round(a + b, 4)
    print(f"The sum of {a} and {b} is {sum}.")
    return f"{a} + {b} = {sum}"

def subtract(a, b):
    # Subtract numbers and return the difference
    diff = round(a - b, 4)
    print(f"The difference of {a} and {b} is {diff}.")
    return f"{a} - {b} = {diff}"

def multiply(a, b):
    # Multiply numbers and return the product
    product = round(a * b, 4)
    print(f"The product of {a} and {b} is {product}.")
    return f"{a} * {b} = {product}"

def divide(a, b):
    # Divide numbers and return the quotient
    # If the user divides by zero, return DIV ERROR
    if b != 0:
        quotient = round(a / b, 4)
        print(f"The quotient of {a} and {b} is {quotient}.")
        return f"{a} / {b} = {quotient}"
    else:
        print("You cannot divide by zero.")
        return "DIV ERROR"

def exponent(a, b):
    # Raise a to the power of b and return the answer
    product = round(a ** b, 4)
    print(f"{a} raised to the power of {b} is {product}.")
    return f"{a} ** {b} = {product}"

# Print welcome message
print("Welcome to the Calculator App!")
print("Enter two numbers and an operation and the desired operation will be performed.")

history = []
while True:
    # Get numbers from the user
    print("")
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    # Check if numbers are actually numbers
    try:
        num1, num2 = float(num1), float(num2)
    except ValueError:
        input("Invalid numbers. ")
        continue

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
        history += ["OP ERROR"]
        continue

    # Check if the user would like to do anothr calculation
    if input("Would you like to do another calculation (y/n)? ").lower().startswith("y") == False:
        print("\nCalculation Summary:")
        for _ in history:
            print(_)
        raise SystemExit