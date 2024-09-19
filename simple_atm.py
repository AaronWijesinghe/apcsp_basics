
import os
import zlib

if os.path.exists("simple_atm_data.py"):
    save = eval(open("simple_atm_data.py").read())
    exec(zlib.decompress(save).decode())
else:
    money = 100

def atm():
    global money

    command = ""
    while command.lower() != "exit":
        print("")
        print(f"[Your balance is: ${money:.2f}]")
        command = input("Choose a command: ").lower()
        if command == "deposit":
            deposit = input("How much to deposit? ").replace("$", "")
            try:
                deposit = float(deposit)
            except:
                input("Invalid amount of money. ")
                continue
            money += float(deposit)
            save = f"money = {money}".encode()
            save = zlib.compress(save)
            open("simple_atm_data.py", "w").write(str(save))

            input(f"Successfully deposited money. Your balance is now ${money:.2f}. ")
        elif command == "withdraw":
            withdraw = input("How much to withdraw? ").replace("$", "")
            try:
                withdraw = float(withdraw)
            except:
                input("Invalid amount of money. ")
                continue

            if money < float(withdraw):
                input(f"Not enough money to withdraw. You need ${withdraw-money:.2f} more to withdraw this amount. ")
                continue
            else:
                money -= float(withdraw)
                save = f"money = {money}".encode()
                save = zlib.compress(save)
                open("simple_atm_data.py", "w").write(str(save))

                input(f"Successfully withdrew money. Your balance is now ${money:.2f}. ")

atm()
