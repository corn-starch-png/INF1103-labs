inventory = []
units_processed = 0
number_of_transactions = 0
failed_attempts = 0
user_input = ""


def get_valid_input():
    stock_input = input("\nEnter a item name to add to inventory (or type 'quit' to exit): ")
    if stock_input == "quit":
        return stock_input, None
    else:
        amt_input = input("Enter the quantity to add: ")
        if amt_input.isdigit():
            quantity = int(amt_input)
            if quantity < 0:
                print("Please enter a positive integer.")
                return None, None
            else:
                return stock_input, quantity
        else:
            print("Invalid input. Please enter a positive integer or 'quit' to exit.")
            return None, None


def process_delivery(current_total, new_value):
    current_total += new_value
    
    if current_total > 500:
        print("Warning: Inventory exceeds 500 units. Consider reducing stock.")
    tax_amount = calculate_tax(new_value)
    print(f"\nOrder updated | Tax for this update: {tax_amount}")
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
    for item in inventory:
        print(f"{item[0]}, {item[1]}, {item[2]}")


def load_inventory():
    inventory = []
    print("Current Orders:")
    try:
        with open("inventory_data.txt", "r") as file:
            data = file.read().splitlines()
        for i in data:
            inventory.append(i.split(","))
        
        for item in inventory:
            print(f"{item[0]}, {item[1]}, {item[2]}")

        
    except FileNotFoundError:
        print("No previous inventory data found. Starting fresh.")

    return inventory
     
  
inventory = load_inventory()
current_id = 1000 + len(inventory)  # Update current_id based on loaded inventory

while user_input != "quit":
    item, quantity = get_valid_input()
    if item == "quit":
        break
    elif item is None:
        failed_attempts += 1
        continue
    else:
        if item not in [i[1] for i in inventory]:
            inventory.append([current_id, item, quantity])
            print("New Order Added:")
            print(f"{current_id}, {item}, {quantity}")
            tax = calculate_tax(quantity)
            print(f"Tax for this order: {tax}")
            current_id += 1
        else:
            for i in inventory:
                if i[1] == item:
                    i[2] = process_delivery(int(i[2]), quantity)
                    print(f"{i[0]}, {i[1]}, {i[2]}")
        number_of_transactions += 1
        units_processed += quantity

    

generate_report(units_processed, failed_attempts)
