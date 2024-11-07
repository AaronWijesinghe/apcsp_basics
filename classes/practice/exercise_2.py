class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        try:
            self.balance += amount
            print(f"Successfully added ${amount} to {self.owner}'s account!")
        except ValueError:
            print("Invalid amount of money.")

    def withdraw(self, amount):
        try:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Successfully withdrawed ${amount} from {self.owner}'s account!")
            else:
                print("Not enough money to withdraw.")
        except ValueError:
            print("Invalid amount of money to withdraw.")

account = BankAccount("Aaron Wijesinghe", 100)
account.deposit(100)
account.withdraw(200)