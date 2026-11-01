import json
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self) -> int:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price
    
    def get_stock(self) -> int:
        return self.__stock
    

    def update_stock(self, quantity: int) -> None:
        self.__stock += quantity

    def display_information(self) -> None:
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    @abstractmethod
    def get_fulfillment_info(self) -> str:
        pass


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """calculate shipping cost based on weight and other factors"""
        pass


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


class DigitalProduct(Product):
    def __init__(self, product_id: int, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} GB")

    def get_fulfillment_info(self) -> str:
        return f"This product is available for immediate download"


class Inventory:
    def __init__(self):
        self.__inventory_list = []

    def add_product(self, product: Product) -> None:
        self.__inventory_list.append(product)

    def search_product(self, name: str) -> None:
        for item in self.__inventory_list:
             if name == item.get_name():
                  return item

    def get_products(self) -> list:
        return self.__inventory_list

    def display_all(self) -> None:
        name_width = max(len("Name"), max(len(item.get_name()) for item in self.__inventory_list)) + 2
        print(f"{'Product ID':<12}| {'Name':<{name_width}}| {'Price':<7}| {'Stock':<7}| ")
        for item in self.__inventory_list:
            print(f"{item.get_product_id():<12}| {item.get_name():<{name_width}}| {item.get_price():<7}| {item.get_stock():<7}| ")


class FileManager:
    @staticmethod
    def load_from_json(file_path: str) -> Inventory:
        inventory = Inventory()
        
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Loop through the list of products in the JSON
            for item_data in data.get("products", []):
                if item_data["type"] == "PhysicalProduct":
                    product = PhysicalProduct(
                        product_id=item_data["id"],
                        name=item_data["name"],
                        price=item_data["price"],
                        stock=item_data["quantity"],
                        weight=item_data["weightorsize"]
                    )
                elif item_data["type"] == "DigitalProduct":
                    product = DigitalProduct(
                        product_id=item_data["id"],
                        name=item_data["name"],
                        price=item_data["price"],
                        stock=item_data["quantity"],
                        download_size=item_data["weightorsize"]
                    )
                else:
                    continue  # Skip unknown product types
                inventory.add_product(product)
                
        return inventory

    @staticmethod
    def save_to_json(inventory: Inventory, file_path: str) -> None:
        products_data = []
        
        for item in inventory.get_products():
            if item.__class__.__name__ == "PhysicalProduct":
                product_dict = {
                    "type": "PhysicalProduct",
                    "id": item.get_product_id(),
                    "name": item.get_name(),
                    "quantity": item.get_stock(),
                    "price": item.get_price(),
                    "weightorsize": item.get_weight()
                }
            elif item.__class__.__name__ == "DigitalProduct":
                product_dict = {
                    "type": "DigitalProduct",
                    "id": item.get_product_id(),
                    "name": item.get_name(),
                    "quantity": item.get_stock(),
                    "price": item.get_price(),
                    "weightorsize": item.get_download_size()
                }
            products_data.append(product_dict)
            
        data = {"products": products_data}
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
