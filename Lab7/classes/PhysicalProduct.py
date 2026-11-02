from classes.Product import Product
from classes.CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: int, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfillment_info(self) -> str:
        return f"This product requires shipping"

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 10.0