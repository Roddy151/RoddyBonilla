from enum import Enum
from collections import defaultdict
from collections import Counter

class OrderStatus(Enum):
    PENDING = 1 
    SHIPPED = 2
    DELIVERED = 3

def check_order_status(status: OrderStatus):
    # Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PENDING:
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "Order has been delivered."

def register_product():

    inventory = defaultdict(int)
    
    while True:
        # Ask the user if they want to add a new item
        add_item = input("Do you want to add a new item to the inventory? (yes/no: )").strip().lower()
        if add_item not in ("yes", "y"):
            print("Inventory management finished.")
            break

        # Ask for the item name
        item = input("Enter the name of the item: ").strip()
        if not item:
            print("Item name connot be empty. Plese try again.")
            continue

        # Ask for the quantity and validate
        try:
            quantity = int(input(f"Enter the quantity of {item}: ").strip())
        except ValueError:
            print("Invalid quantity. Please enter a number. Try again.")
            continue

        # Add the item to the inventory
        inventory[item] += quantity
        print(f"Item {item} updated. Total quantity: {inventory[item]}")
    # Check if the inventory is empty
    if not inventory:
        print("\nNo items were added to the inventory.")
    else:
        # Display the final inventory
        print("\nFinal inventory:")
        for item, quantity in inventory.items():
            print(f"- {item}: {quantity}")

# Call the funtion to start inventory management
register_product()


        
              