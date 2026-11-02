from classes.Product import Product


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
