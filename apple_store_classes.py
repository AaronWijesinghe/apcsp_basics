class Computer():
    def __init__(self, name, cpu, gpu, memory, storage):
        self.name = name
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory
        self.storage = storage

    def print_specs(self):
        print(f"\nHere are the specs for the {self.name}:")
        print(f"CPU: {self.cpu}")
        print(f"GPU: {self.gpu}")
        print(f"Memory: {self.memory}")
        print(f"Storage: {self.storage}")

class MacBook_Air(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        super().__init__(name, cpu, gpu, memory, storage)

class MacBook_Pro13(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        super().__init__(name, cpu, gpu, memory, storage)

class MacBook_Pro16(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        super().__init__(name, cpu, gpu, memory, storage)

class iMac(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        super().__init__(name, cpu, gpu, memory, storage)

class MacPro(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        super().__init__(name, cpu, gpu, memory, storage)

class MacMini(Computer):
    def __init__(self, name, cpu, gpu, memory, storage):
        super().__init__(name, cpu, gpu, memory, storage)

MBA = [
    MacBook_Air("MacBook Air", "Apple M2", "Integrated 7-core GPU", "8GB", "256GB SSD"),
    MacBook_Air("MacBook Air", "Apple M3", "Integrated 7-core GPU", "8GB", "256GB SSD")
]

MBP13 = [
    MacBook_Pro13("MacBook Pro 13-inch", "Apple M2 Pro", "Integrated 14-core GPU", "16GB", "512GB SSD"),
    MacBook_Pro13("MacBook Pro 13-inch", "Apple M3 Pro", "Integrated 14-core GPU", "16GB", "512GB SSD")
]

MBP16 = [
    MacBook_Pro16("MacBook Pro 16-inch", "Apple M2 Pro", "Integrated 16-core GPU", "16GB", "512GB SSD"),
    MacBook_Pro16("MacBook Pro 16-inch", "Apple M3 Pro", "Integrated 16-core GPU", "16GB", "512GB SSD"),
    MacBook_Pro16("MacBook Pro 16-inch", "Apple M2 Max", "Integrated 16-core GPU", "32GB", "1TB SSD"),
    MacBook_Pro16("MacBook Pro 16-inch", "Apple M3 Max", "Integrated 16-core GPU", "32GB", "1TB SSD")
]

iMacs = [
    iMac("iMac 24-inch", "Apple M2", "Integrated 7-core GPU", "8GB", "256GB SSD"),
    iMac("iMac 24-inch", "Apple M3", "Integrated 7-core GPU", "8GB", "256GB SSD"),
]

MacPros = [
    MacPro("Mac Pro", "Apple M2 Max", "Integrated 16-core GPU", "32GB", "1TB SSD"),
    MacPro("Mac Pro", "Apple M3 Max", "Integrated 16-core GPU", "32GB", "1TB SSD"),
    MacPro("Mac Pro", "Apple M2 Ultra", "Integrated 16-core GPU", "192GB", "8TB SSD"),
]

MacMinis = [
    MacMini("Mac Mini", "Apple M2", "Integrated 7-core GPU", "8GB", "256GB SSD"),
    MacMini("Mac Mini", "Apple M3", "Integrated 7-core GPU", "8GB", "256GB SSD")
]

print("Welcome to the Apple Store!")
if not input("Are you looking for an Apple product? ").lower().startswith("y"):
    raise SystemExit

print("1) MacBook Air")
print("2) MacBook Pro 13-inch")
print("3) MacBook Pro 16-inch")
print("4) iMac")
print("5) Mac Pro")
print("6) Mac Mini")

try:
    choice = int(input("Which product would you like to see? "))
except ValueError:
    choice = 0

if choice == 1:
    for macbook_air in MBA:
        macbook_air.print_specs()
elif choice == 2:
    for macbook_pro13 in MBP13:
        macbook_pro13.print_specs()
elif choice == 3:
    for macbook_pro16 in MBP16:
        macbook_pro16.print_specs()
elif choice == 4:
    for imac in iMacs:
        imac.print_specs()
elif choice == 5:
    for mac_pro in MacPros:
        mac_pro.print_specs()
elif choice == 6:
    for mac_mini in MacMinis:
        mac_mini.print_specs()
