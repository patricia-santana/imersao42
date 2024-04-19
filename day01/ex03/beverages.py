class HotBeverage:
    def __init__(self, name="hot beverage", price=0.50, description="Just some hot water in a cup."):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.price}€): {self.description}"

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(name="coffee", price=1.00, description="A coffee, to stay awake.")

class Tea(HotBeverage):
    def __init__(self):
        super().__init__(name="tea", price=0.80, description="A nice hot tea.")
