import json
from classes.Product import Product
from classes.Inventory import Inventory

class FileManager:
    @staticmethod
    def load_from_json(file_path: str) -> Inventory:
        inventory = Inventory()
        
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Loop through the list of products in the JSON
            for item_data in data.get("products", []):
                product = Product(
                    product_id=item_data["id"],
                    name=item_data["name"],
                    price=item_data["price"],
                    stock=item_data["quantity"]
                )
                inventory.add_product(product)
                
        return inventory

    @staticmethod
    def save_to_json(inventory: Inventory, file_path: str) -> None:
        products_data = []
        
        for item in inventory.get_products():      
            product_dict = {
                "id": item.get_product_id(),
                "name": item.get_name(),
                "quantity": item.get_stock(),
                "price": item.get_price()
            }
            products_data.append(product_dict)
            
        data = {"products": products_data}
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)