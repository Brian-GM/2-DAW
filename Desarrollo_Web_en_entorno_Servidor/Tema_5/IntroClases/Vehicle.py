class Vehicle:
    latin: str = "Lore Ipsum"
    def __init__(self, brand: str, color: str) -> None:
        self.brand: str = brand
        self.color: str = color

    def display_info(self) -> None:
        print("Soy un vehiculo")


class Car(Vehicle):
    def __init__(self, doors: int, brand: str, color: str) -> None:
        super().__init__(brand, color)
        self.doors: int = doors


class Bike(Vehicle):
    def __init__(self, gear: int, brand: str, color: str) -> None:
        super().__init__(gear,brand, color)
        self.gear: int = gear

    def display_info(self) -> None:
        super().display_info()
        print("Soy una bicileta")
