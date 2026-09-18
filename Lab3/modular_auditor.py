inventory = 0
number_of_deliveries = 0
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
    current_total += new_value
    print(f"Added {new_value} to inventory. Current inventory: {current_total}")
    tax_amount = calculate_tax(new_value)
    print(f"Tax for this delivery: {tax_amount}")
    return current_total


def calculate_tax(amount):
    tax_rate = 0.1  # 10% tax rate
    tax_amount = amount * tax_rate
    return tax_amount


def generate_report(total_units, failed_attempts):
    print(f"Final inventory: {total_units}")
    print(f"Total deliveries processed: {number_of_deliveries}")
    print(f"Total failed attempts to add stock: {failed_attempts}")



while user_input != "quit":
    user_input = get_valid_input()
    if user_input == "quit":
        break
    elif user_input is None:
        failed_attempts += 1
        continue
    else:
        inventory = process_delivery(inventory, user_input)
        number_of_deliveries += 1

    #requriement 7 overstock alert
    if inventory > 500:
        print("Warning: Inventory exceeds 500 units. Consider reducing stock.")
        break

generate_report(inventory, failed_attempts)