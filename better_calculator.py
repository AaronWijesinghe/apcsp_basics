import sys
sys.set_int_max_str_digits(0)

bold = "\033[1m"
underline = "\033[4m"
end = "\033[0m"

# You don't actually need 5 functions to do this
def calc(operation, a, b):
    global history

    try:
        sum = round(eval(f"a {operation} b"), 4)
        print(f"{a} {operation} {b} = {sum}")
        history += [f"{a} {operation} {b} = {sum}"]
    except ZeroDivisionError:
        print(f"{bold}You cannot divide by zero.{end}")
        history += ["DIV ERROR"]
    except OverflowError:
        print(f"{bold}Result is too large to display. This can be solved by not using decimals.{end}")
        history += ["OVERFLOW ERROR"]

print(f"{bold}Welcome to the Calculator App!{end}")
print("Enter two numbers and an operation and the desired operation will be performed.")

history = []
while True:
    try:
        # Get numbers from the user and set their types accordingly
        print("")
        num1 = input("Enter a number: ")
        num2 = input("Enter another number: ")
        if not "." in num1 or "." in num2:
            num1, num2 = int(num1), int(num2)
        else:
            num1, num2 = float(num1), float(num2)


        # Get operation from the user
        operation = input("Enter an operation (addition, subtraction, multiplication, division, or exponentation): ").lower().strip()

        # Perform calculations and save the result to history
        if operation in ["addition", "a"]:
            calc("+", num1, num2)
        elif operation in ["subtraction", "s"]:
            calc("-", num1, num2)
        elif operation in ["multiplication", "m"]:
            calc("*", num1, num2)
        elif operation in ["division", "d"]:
            calc("/", num1, num2)
        elif operation in ["exponentation", "e"]:
            calc("**", num1, num2)
        else:
            print(f"{bold}This operation doesn't exist.{end}")
            history += ["OP ERROR"]
    except ValueError:
        print("Invalid numbers. ")

    if not input("Would you like to do another calculation (y/n)? ").lower().startswith("y"):
        print(f"\n{underline}Calculation Summary:{end}")
        for _ in history:
            print(_)
        if len(history) == 0:
            print("No calculations saved!")
        raise SystemExit