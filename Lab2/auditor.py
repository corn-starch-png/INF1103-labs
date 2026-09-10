inventory = 0
user_input = ""

while user_input != "quit":
    user_input = input("Enter a stock quantity to add to inventory (or type 'quit' to exit): ")
    if user_input == "quit":
        break
    if user_input.isdigit():
        quantity = int(user_input)
        inventory += quantity
        print(f"Added {quantity} to inventory. Current inventory: {inventory}")
    else:
        print("Invalid input. Please enter a positive integer or 'quit' to exit.")
print(f"Final inventory: {inventory}")