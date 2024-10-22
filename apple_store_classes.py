# The clear() function won't work in PyCharm.
# Use another terminal for the best experience.

# Import modules that will add extra functionality
import os
import copy
import platform

# Platform-agnostic clear console function
# I am testing this program on Windows and macOS, so this is required!
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# ANSI escape codes for bold text
bold = "\033[1m"
end = "\033[0m"

# Class detailing the specs of a computer, which will be used in subclasses later on
# This includes the tools required to print specifications and apply device upgrades
class Computer:
    def __init__(self, name, cpu, gpu, memory, storage, price):
        self.name = name
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory
        self.storage = storage
        self.price = price

    def print_specs(self):
        print(f"\n{bold}[ID: {itemsFound}] {self.name}{end}")
        print(f"    - CPU: {self.cpu}")
        print(f"    - GPU: {self.gpu}")
        print(f"    - Memory: {self.memory}")
        print(f"    - Storage: {self.storage}")
        print(f"    - Price: ${self.price}")

    def apply_upgrade(self, priceIncrease, category, upgrade):
        self.price += priceIncrease
        exec(f"self.{category} = upgrade")

# All of the Apple devices available in the store will be listed below.
class MacBook_Air(Computer):
    def __init__(self, name, cpu, gpu, memory, storage, price):
        super().__init__(name, cpu, gpu, memory, storage, price)

class MacBook_Pro14(Computer):
    def __init__(self, name, cpu, gpu, memory, storage, price):
        super().__init__(name, cpu, gpu, memory, storage, price)

class MacBook_Pro16(Computer):
    def __init__(self, name, cpu, gpu, memory, storage, price):
        super().__init__(name, cpu, gpu, memory, storage, price)

class iMac(Computer):
    def __init__(self, name, cpu, gpu, memory, storage, price):
        super().__init__(name, cpu, gpu, memory, storage, price)

class MacPro(Computer):
    def __init__(self, name, cpu, gpu, memory, storage, price):
        super().__init__(name, cpu, gpu, memory, storage, price)

class MacMini(Computer):
    def __init__(self, name, cpu, gpu, memory, storage, price):
        super().__init__(name, cpu, gpu, memory, storage, price)

class iPhone(Computer):
    def __init__(self, name, cpu, gpu, memory, storage, price):
        super().__init__(name, cpu, gpu, memory, storage, price)

# This is a list of all the BASE MODEL Apple computers available in the store.
computers = [
    [
        MacBook_Air("MacBook Air", "Apple M2", "8-core GPU", "8GB", "256GB SSD", 999),
        MacBook_Air("MacBook Air", "Apple M3", "8-core GPU", "8GB", "256GB SSD", 1099)
    ],
    [
        MacBook_Pro14("MacBook Pro 14-inch", "Apple M3 Pro", "14-core GPU", "18GB", "512GB SSD", 1999),
        MacBook_Pro14("MacBook Pro 14-inch", "Apple M3 Max", "30-core GPU", "36GB", "1TB SSD", 3199)
    ],
    [
        MacBook_Pro16("MacBook Pro 16-inch", "Apple M3 Pro", "14-core GPU", "18GB", "512GB SSD", 2899),
        MacBook_Pro16("MacBook Pro 16-inch", "Apple M3 Max", "30-core GPU", "36GB", "1TB SSD", 3499)
    ],
    [
        iMac("iMac 24-inch", "Apple M3", "8-core GPU", "8GB", "256GB SSD", 1299),
    ],
    [
        MacPro("Mac Pro", "Apple M1 Ultra", "48-core GPU", "64GB", "1TB SSD", 5999),
        MacPro("Mac Pro", "Apple M2 Ultra", "60-core GPU", "64GB", "1TB SSD", 6999),
    ],
    [
        # Got rid of 2 GPU cores to make the upgrade that you will see later on make more sense.
        MacMini("Mac Mini", "Apple M2", "8-core GPU", "8GB", "256GB SSD", 599),
    ],
    [
        # For the sake of simplicity, the iPhone 16 Pro Max will not have the 256 GB of storage it's supposed to have.
        # I decreased the price (Apple never does this) to make up for the missing storage.
        iPhone("iPhone 16", "Apple A18", "5-core GPU", "8GB", "128GB SSD", 799),
        iPhone("iPhone 16 Plus", "Apple A18", "5-core GPU", "8GB", "128GB SSD", 899),
        iPhone("iPhone 16 Pro", "Apple A18 Pro", "6-core GPU", "8GB", "128GB SSD", 999),
        iPhone("iPhone 16 Pro Max", "Apple A18 Pro", "6-core GPU", "8GB", "128GB SSD", 1099)
    ]
]

# These are the possible upgrades that can be applied to each Apple device.
# Each upgrade is CPU specific, so the upgrade options are different for each device.
possible_upgrades = {
    "Apple M3": [
        {"gpu": "10-core GPU", "price": 200},
        {"memory": "16GB", "price": 200},
        {"memory": "24GB", "price": 400},
        {"storage": "512GB SSD", "price": 200},
        {"storage": "1TB SSD", "price": 400},
        {"storage": "2TB SSD", "price": 800}
    ],
    "Apple M3 Pro": [
        {"gpu": "18-core GPU", "price": 200},
        {"memory": "36GB", "price": 400},
        {"storage": "1TB SSD", "price": 200},
        {"storage": "2TB SSD", "price": 600},
        {"storage": "4TB SSD", "price": 1200}
    ],
    "Apple M3 Max": [
        {"gpu": "40-core GPU", "price": 300},
        {"memory": "48GB", "price": 200},
        {"memory": "64GB", "price": 400},
        {"memory": "96GB", "price": 800},
        {"memory": "128GB", "price": 1200},
        {"storage": "2TB SSD", "price": 400},
        {"storage": "4TB SSD", "price": 1000},
        {"storage": "8TB SSD", "price": 2200}
    ],
    "Apple M1 Ultra": [
        {"gpu": "64-core GPU", "price": 1000},
        {"memory": "96GB", "price": 800},
        {"memory": "128GB", "price": 1600},
        {"storage": "2TB SSD", "price": 400},
        {"storage": "4TB SSD", "price": 1000},
        {"storage": "8TB SSD", "price": 2200}
    ],
    "Apple M2 Ultra": [
        {"gpu": "76-core GPU", "price": 1000},
        {"memory": "128GB", "price": 800},
        {"memory": "192GB", "price": 1600},
        {"storage": "2TB SSD", "price": 400},
        {"storage": "4TB SSD", "price": 1000},
        {"storage": "8TB SSD", "price": 2200}
    ],
    "Apple A18": [
        {"storage": "256GB SSD", "price": 100},
        {"storage": "512GB SSD", "price": 300}
    ],
    "Apple A18 Pro": [
        {"storage": "256GB SSD", "price": 100},
        {"storage": "512GB SSD", "price": 300},
        {"storage": "1TB SSD", "price": 500}
    ]
}
possible_upgrades["Apple M2"] = possible_upgrades["Apple M3"]
possible_upgrades["Apple M2 Pro"] = possible_upgrades["Apple M3 Pro"]

status = None
while True:
    clear()
    if status == "returning":
        print("Welcome back to the Apple Store, returning customer!")
        welcomePrompt = "Want to buy another Apple product (y/n)? "
    elif status == "no_purchase":
        print("Welcome back! Still thinking of buying an Apple product?")
        welcomePrompt = "Want to go back into the store (y/n)? "
    else:
        print("Welcome to the Apple Store!")
        welcomePrompt = "Are you looking for an Apple product (y/n)? "

    if not input(welcomePrompt).lower().startswith("y"):
        break

    # Print selection of Apple products
    print(f"\n{bold}Here is our selection of Apple products:{end}")
    print("[1] MacBook Air")
    print("[2] MacBook Pro 14-inch")
    print("[3] MacBook Pro 16-inch")
    print("[4] iMac")
    print("[5] Mac Pro")
    print("[6] Mac Mini")
    print("[7] iPhone")

    # Get user input on which product they want to view
    choice = input(f"\nChoose a number from 1-{len(computers)} to view that specific product: ").strip()

    # Print the products available for sale, alongside their specs
    itemsFound = 0
    if choice.isnumeric():
        choice = int(choice) - 1
        if abs(choice) >= len(computers):
            status = "no_purchase"
            input("This product doesn't exist. ")
            continue
        else:
            clear()
            print(f"Here are the models of the {bold}{computers[choice][0].name}{end} currently available for sale:")

        for product in computers[choice]:
            itemsFound += 1
            product.print_specs()
    else:
        status = "no_purchase"
        input("This product doesn't exist. ")
        continue

    # Allow the user to view another product or buy the product they are currently viewing
    id = input("\nPress ENTER to view another product, or type a Product ID to buy it. ")
    if id.isnumeric() and int(id) <= itemsFound:
        clear()
        id = int(id) - 1
        product = copy.deepcopy(computers[choice][id])

        # Show the user device upgrades that can be applied
        print(f"Here are some upgrades that can be applied to your {bold}{product.name}{end}:")
        upgrades = 0
        for upgrade in possible_upgrades[product.cpu]:
            upgrades += 1
            if "gpu" in upgrade:
                print(f"    - [{upgrades}] {product.gpu} -> {bold}{upgrade['gpu']}{end} (${upgrade['price']})")
            elif "memory" in upgrade:
                print(f"    - [{upgrades}] {product.memory} Memory -> {bold}{upgrade['memory']} Memory{end} (${upgrade['price']})")
            elif "storage" in upgrade:
                print(f"    - [{upgrades}] {product.storage} -> {bold}{upgrade['storage']}{end} (${upgrade['price']})")

        # Ask the user which upgrades they want to apply to their device, and apply them
        print("\nThings to keep in mind when upgrading a product:")
        print(f"    - Each upgrade should be {bold}seperated with a comma{end} (ex: 1, 2, 3).")
        print(f"    - You may only buy {bold}one{end} of each upgrade type.")
        print("    - You can always press ENTER without entering anything to skip this step.")
        upgrades = input("\nEnter the upgrades you want to purchase: ").replace(" ", "").strip()
        if upgrades.isnumeric() or "," in upgrades:
            alreadyUpgradedComponents = []
            upgrades = upgrades.split(",")
            for upgrade in upgrades:
                upgrade = int(upgrade) - 1
                try:
                    component = list(possible_upgrades[product.cpu][upgrade])[0]
                    if not component in alreadyUpgradedComponents:
                        previous_component = eval(f"product.{component}")
                        product.apply_upgrade(possible_upgrades[product.cpu][upgrade]["price"], component, possible_upgrades[product.cpu][upgrade][component])
                        alreadyUpgradedComponents += [component]
                        exec(f"product.{component} = '{previous_component} -> {bold}'+product.{component}+'{end}'")
                except:
                    pass

            # Print new specs and prompt the user to buy the device
            clear()
            print("Upgrades successfully applied! Here are your device's new specs:")
        else:
            clear()
            print("Alright, no upgrades were applied. Here are your device's specs:")

        product.print_specs()
        if input("\nDo you want to buy this device (y/n)? ").lower().strip().startswith("y"):
            status = "returning"
            input(f"You purchased the {product.name} for ${product.price}! ")
        else:
            status = "no_purchase"
            input("Purchase cancelled. ")
    else:
        status = "no_purchase"
        input("Invalid Product ID. ")