inventory = 0
failed_attempts = 0
user_input = ""


def get_valid_input():
    user_input = input("Enter a stock quantity to add to inventory (or type 'quit' to exit): ")
    if user_input == "quit":
        return user_input
    if user_input.isdigit():
        quantity = int(user_input)
        if quantity < 0:
            print("Please enter a positive integer.")
            return None
        else:
            return quantity
    else:
        print("Invalid input. Please enter a positive integer or 'quit' to exit.")
        return None


def process_delivery(current_total, new_value):
    pass


def calculate_tax(amount):
    pass


def generate_report(total_units, failed_attempts):
    pass



while user_input != "quit":
    user_input = get_valid_input()
    if user_input == "quit":
        break
    elif user_input is None:
        failed_attempts += 1
        continue
    else:
        quantity = user_input
        inventory += quantity
        print(f"Added {quantity} to inventory. Current inventory: {inventory}")
        
    #requriement 7 overstock alert
    if inventory > 500:
        print("Warning: Inventory exceeds 500 units. Consider reducing stock.")
        break
    
print(f"Final inventory: {inventory}")
print(f"Total failed attempts to add stock: {failed_attempts}")