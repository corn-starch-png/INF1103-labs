from classes import Product, Inventory, FileManager
units_processed = 0
number_of_transactions = 0
failed_attempts = 0
user_input = ""



def add_product(current_id,number_of_transactions, units_processed, failed_attempts):
    def get_new_product():
        item_name = input("\nEnter a item name to add to inventory (or type 'quit' to exit): ")
        if item_name == "quit":
            return item_name, None, None
        else:
            amt_input = input("Enter the quantity to add: ")
            if amt_input.isdigit():
                quantity = int(amt_input)
                if quantity < 0:
                    print("Please enter a positive integer.")
                    return None, None, None
            else:
                print("Invalid input. Please enter a positive integer")
                return None, None, None

            price_input = input("Enter the price of the item: ")
            if price_input.replace('.', '', 1).isdigit():
                price = float(price_input)
                if price < 0:
                    print("Please enter a positive number.")
                    return None, None, None
            else:
                print("Invalid input. Please enter a positive number.")
                return None, None, None
        
        return item_name, quantity, price


    item_name, quantity, price = get_new_product()
    if item_name == "quit":
        return
    elif item_name is None or quantity is None or price is None:
        failed_attempts += 1
        return
    else:
        existing_product = inventory.search_product(item_name)
        if not existing_product:
            product = Product(current_id, item_name, quantity, price)
            inventory.add_product(product)
            print("New Product Added:")
            product.display_information()

            tax = calculate_tax(quantity * price)
            print(f"Tax for this product: ${tax:.2f}")

            current_id += 1
            number_of_transactions += 1
            units_processed += quantity
        else:
            print("[ERROR] Product already exists. Please use update option to modify the quantity.")
            failed_attempts += 1
    return



def update_stock(number_of_transactions, units_processed, failed_attempts):
    inventory.display_all()
    name_input = input("\nEnter item name to update inventory (or type 'quit' to exit): ")
    if name_input == "quit":
        return
    item = inventory.search_product(name_input)
    if item:
        print("Product found.")
        item.display_information()
        amt_input = input("Enter the quantity to add: ")
        if amt_input.isdigit():
            quantity = int(amt_input)
            if quantity < 0:
                print("Please enter a positive integer.")
                failed_attempts += 1
                return
        else:
            print("Invalid input. Please enter a positive integer")
            failed_attempts += 1
            return 
        
        item.update_stock(quantity)
        tax = calculate_tax(quantity*item.get_price())
        print(f"Stock updated successfully. Note additional ${tax:.2f} tax")
        number_of_transactions += 1
        units_processed += quantity
        return
    else:    
        print("Product not found.")
        failed_attempts += 1
        return



def search_product():
    product_name = input("\nEnter the product name to search (or type 'quit' to exit): ")
    item = inventory.search_product(product_name)
    if item:
        item.display_information()
    else:
        print("Product not found.")



def process_delivery(current_total, new_value, price):
    current_total += new_value
    
    if current_total > 500:
        print("Warning: Inventory exceeds 500 units. Consider reducing stock.")
    tax_amount = calculate_tax(new_value * price)
    print(f"\nProduct updated | Tax for this update: ${tax_amount:.2f}")
    return current_total


def calculate_tax(amount):
    tax_rate = 0.1  # 10% tax rate
    tax_amount = amount * tax_rate
    return tax_amount


def generate_report(total_units, failed_attempts):
    print("\n---------Inventory Report---------")
    print(f"Total units processed: {total_units}")
    print(f"Total transactions processed: {number_of_transactions}")
    print(f"Total failed attempts to add stock: {failed_attempts}")
    print("\nFinal Inventory:")
    print("id, Name, Quantity, Price")
    for item in inventory["products"]:
        print(f"{item['id']}, {item['name']}, {item['quantity']}, {item['price']}")
    print("-----------------------------------")


def load_inventory():
    print("Current Orders:")
    try:
        with open("inventory_data.json", "r") as file:
            data = json.load(file)
        print("Loaded inventory from inventory_data.json")
      
    except FileNotFoundError:
        print("No previous inventory data found. Starting fresh.")
        data = { "products": [] }

    return data


def display_all():
    print("\nCurrent Inventory:")
    print("-----------------------------")
    print("ID, Name, Quantity, Price")
    for item in inventory["products"]:
        print(f"{item['id']}, {item['name']}, {item['quantity']}, {item['price']}")
    print("-----------------------------")


def save_inventory(inventory):
    with open("inventory_data.json", "w") as file:
        json.dump(inventory, file)
    print("Inventory saved to inventory_data.json")

print("==========================================")
print("Welcome to the Inventory Management System")
print("==========================================")

inventory = load_inventory()
current_id = 1000 + len(inventory["products"])  # Update current_id based on loaded inventory

while user_input != "6":
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        display_all()
    elif user_input == "2":
        add_product(current_id, number_of_transactions, units_processed, failed_attempts)
    elif user_input == "3":
        update_stock(number_of_transactions, units_processed, failed_attempts)
    elif user_input == "4":
        search_product()
    elif user_input == "5":
        save_inventory(inventory)
    elif user_input == "6":
        break
    else:
        print("Invalid choice. Please try again.")

save_inventory(inventory)
generate_report(units_processed, failed_attempts)
print("Exiting the program. Goodbye!")
