import random
from beverages import HotBeverage, Coffee, Tea

class BrokenMachineException(Exception):
    def __init__(self):
        super().__init__("This coffee machine has to be repaired.")

class EmptyCup(HotBeverage):
    def __init__(self):
        super().__init__(name="empty cup", price=0.90, description="An empty cup?! Gimme my money back!")

class CoffeeMachine:
    def __init__(self):
        self.counter = 0
        self.is_broken = False

    def repair(self):
        print("Repairing the coffee machine...")
        self.counter = 0
        self.is_broken = False

    def serve(self, beverage_class):
        if self.is_broken:
            raise BrokenMachineException()
        if self.counter >= 10:
            self.is_broken = True
            raise BrokenMachineException()
        self.counter += 1
        if random.choice([True, False]):
            return beverage_class()
        else:
            return EmptyCup()

if __name__ == "__main__":
    machine = CoffeeMachine()
    beverages = [Coffee, Tea]
    while True:
        try:
            beverage = random.choice(beverages)
            served_beverage = machine.serve(beverage)
            print(served_beverage)
        except BrokenMachineException as e:
            print(e)
            repair_choice = input("Do you want to repair the machine? (yes/no): ")
            if repair_choice.lower() == 'no':
                break
            machine.repair()
