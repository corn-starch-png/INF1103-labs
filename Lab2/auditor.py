inventory = 0
user_input = ""

while user_input != "quit":
    user_input = input("Enter a stock quantity to add to inventory (or type 'quit' to exit): ")
    if user_input == "quit":
        break
print(f"Final inventory: {inventory}")