import json
from classes.PhysicalProduct import PhysicalProduct
from classes.DigitalProduct import DigitalProduct
from classes.Inventory import Inventory

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