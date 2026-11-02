from classes.Product import Product

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
