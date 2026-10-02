import json
units_processed = 0
number_of_transactions = 0
failed_attempts = 0
user_input = ""


def get_new_product():
    stock_input = input("\nEnter a item name to add to inventory (or type 'quit' to exit): ")
    if stock_input == "quit":
        return stock_input, None, None
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
    

    return stock_input, quantity, price


def new_product():
    item, quantity, price = get_new_product()
    if item == "quit":
        return
    elif item is None or quantity is None or price is None:
        failed_attempts += 1
        return
    else:
        if item not in [i["name"] for i in inventory["products"]]:
            inventory["products"].append({"id": current_id, "name": item, "quantity": quantity, "price": price})
            print("New Product Added:")
            print(f"{current_id}, {item}, {quantity}, {price}")
            tax = calculate_tax(quantity * price)
            print(f"Tax for this product: ${tax:.2f}")
            current_id += 1
            number_of_transactions += 1
            units_processed += quantity
        else:
            print("Product already exists. Please use update option to modify the quantity.")
            failed_attempts += 1
    return


def get_update_product():
    id_input = input("\nEnter a item code to update in inventory (or type 'quit' to exit): ")
    if id_input == "quit":
        return id_input, None
    else:
        amt_input = input("Enter the quantity to add: ")
        if amt_input.isdigit():
            quantity = int(amt_input)
            if quantity < 0:
                print("Please enter a positive integer.")
                return None, None
        else:
            print("Invalid input. Please enter a positive integer")
            return None, None

    return id_input, quantity


def update_product():
    item, quantity = get_update_product()
    if item == "quit":
        return
    for i in inventory["products"]:
        if i["name"] == item:
            print("Product found. Updating quantity...")
            i["quantity"] = process_delivery(i["quantity"], quantity, i["price"])
            print(f"New quantity for {item}: {i['quantity']}")
            print("Stock updated successfully.")
            return
        
    print("Product not found.")
    return


def search_product():
    pass  # Placeholder for search functionality


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
    print(f"Total units processed: {total_units}")
    print(f"Total transactions processed: {number_of_transactions}")
    print(f"Total failed attempts to add stock: {failed_attempts}")
    print("\nFinal Inventory:")
    for item in inventory["products"]:
        print(f"{item['id']}, {item['name']}, {item['quantity']}, {item['price']}")


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


def display_inventory():
    print("\nCurrent Inventory:")
    print("-----------------------------")
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
        display_inventory()
    elif user_input == "2":
        new_product()
    elif user_input == "3":
        update_product()
    elif user_input == "4":
        search_product()
    elif user_input == "5":
        save_inventory(inventory)
    elif user_input == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

save_inventory(inventory)
generate_report(units_processed, failed_attempts)
