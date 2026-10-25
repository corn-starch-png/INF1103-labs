class Product:
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
