from uuid import uuid4


class Product:
    def __init__(self, name: str, description: str, price: float) -> None:
        self.__uuid: str = str(uuid4())
        self.__name: str = name
        self.__description: str = description
        self.__price: float = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> float:
        return self.__price

    @property
    def uuid(self) -> str:
        return self.__uuid

    def __str__(self) -> str:
        return f"Name: {self.__name} UUID: ({self.__uuid}) Description: {self.__description} Price: {self.__price}"

    def __repr__(self) -> str:
        return f"Product(name='{self.__name}', description='{self.__description}', price={self.__price})"


class ShoppingCart:
    def __init__(self) -> None:
        self.__products: list[str] = []

    def total_price(self) -> float:
        total_price: float = 0
        for product in self.__products:
            total_price += product.price
        return total_price

    @property
    def products(self) -> list[str]:
        return self.__products

    def add_product(self, p: Product):
        self.__products.append(p)

    def remove_product(self, p: Product) -> None:
        updated_products = []
        for product in self.__products:
            if product.uuid != p.uuid:
                updated_products.append(product)
        self.__products = updated_products
