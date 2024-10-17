bold = "\033[1m"
underline = "\033[4m"
end = "\033[0m"

class Computer():
    def __init__(self, name, cpu, gpu, memory, storage, price):
        self.name = name
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory
        self.storage = storage
        self.price = price

    def print_specs(self):
        print(f"\n{bold}Device: {self.name}{end}")
        print(f"CPU: {self.cpu}")
        print(f"GPU: {self.gpu}")
        print(f"Memory: {self.memory}")
        print(f"Storage: {self.storage}")
        print(f"Price: {self.price}")

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

computers = [
    [
        MacBook_Air("MacBook Air", "Apple M2", "Integrated 8-core GPU", "8GB", "256GB SSD", "999"),
        MacBook_Air("MacBook Air", "Apple M3", "Integrated 8-core GPU", "8GB", "256GB SSD", "1099")
    ],
    [
        MacBook_Pro14("MacBook Pro 14-inch", "Apple M2 Pro", "Integrated 16-core GPU", "16GB", "512GB SSD", "1499"),
        MacBook_Pro14("MacBook Pro 14-inch", "Apple M3 Pro", "Integrated 14-core GPU", "18GB", "512GB SSD", "1999"),
        MacBook_Pro14("MacBook Pro 14-inch", "Apple M2 Max", "Integrated 16-core GPU", "32GB", "1TB SSD", "2599"),
        MacBook_Pro14("MacBook Pro 14-inch", "Apple M3 Max", "Integrated 16-core GPU", "36GB", "1TB SSD", "3199")
    ],
    [
        MacBook_Pro16("MacBook Pro 16-inch", "Apple M2 Pro", "Integrated 16-core GPU", "16GB", "512GB SSD", "1899"),
        MacBook_Pro16("MacBook Pro 16-inch", "Apple M3 Pro", "Integrated 14-core GPU", "18GB", "512GB SSD", "2499"),
        MacBook_Pro16("MacBook Pro 16-inch", "Apple M2 Max", "Integrated 16-core GPU", "32GB", "1TB SSD", "2899"),
        MacBook_Pro16("MacBook Pro 16-inch", "Apple M3 Max", "Integrated 16-core GPU", "36GB", "1TB SSD", "3499")
    ],
    [
        iMac("iMac 24-inch", "Apple M3", "Integrated 8-core GPU", "8GB", "256GB SSD", "1299")
    ],
    [
        MacPro("Mac Pro", "Apple M2 Max", "Integrated 16-core GPU", "32GB", "1TB SSD", ""),
        MacPro("Mac Pro", "Apple M3 Max", "Integrated 16-core GPU", "32GB", "1TB SSD", ""),
        MacPro("Mac Pro", "Apple M2 Ultra", "Integrated 16-core GPU", "192GB", "8TB SSD", "")
    ],
    [
        MacMini("Mac Mini", "Apple M2", "Integrated 8-core GPU", "8GB", "256GB SSD", ""),
        MacMini("Mac Mini", "Apple M3", "Integrated 8-core GPU", "8GB", "256GB SSD", "")
    ]
]

while True:
    print("Welcome to the Apple Store!")
    if not input("Are you looking for an Apple product (y/n)? ").lower().startswith("y"):
        raise SystemExit

    print("\nHere is our selection of Apple products:")
    print("1) MacBook Air")
    print("2) MacBook Pro 14-inch")
    print("3) MacBook Pro 16-inch")
    print("4) iMac")
    print("5) Mac Pro")
    print("6) Mac Mini")

    try:
        choice = int(input("\nWhich product would you like to see? ")) - 1
    except ValueError:
        choice = len(computers)

    if abs(choice) >= len(computers):
        print("Invalid choice.")
        raise SystemExit
    else:
        print("Here are the products currently available for sale:")

    for product in computers[choice]:
        product.print_specs()