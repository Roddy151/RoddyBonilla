from collections import Counter
from enum import Enum


class OrderStatus(Enum):
    """
    Enum to represent the status of an order.
    """
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3


class Inventory:
    """
    Class to manage inventory operations like adding, removing, and checking items.
    """

    def __init__(self):
        self.items = Counter()

    def add_item(self, item_name, quantity):
        """
        Add items to the inventory.

        :param item_name: Name of the item to add.
        :param quantity: Quantity of the item to add.
        """
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        self.items[item_name] += quantity
        print(f"Item '{item_name}' added to inventory. Total: {self.items[item_name]}")

    def remove_item(self, item_name, quantity):
        """
        Remove items from the inventory.

        :param item_name: Name of the item to remove.
        :param quantity: Quantity of the item to remove.
        :return: True if the removal was successful, False otherwise.
        """
        if item_name not in self.items or self.items[item_name] < quantity:
            print(f"Not enough '{item_name}' in inventory. Available: {self.items.get(item_name, 0)}")
            return False
        self.items[item_name] -= quantity
        return True

    def show_inventory(self):
        """
        Display the current inventory.
        """
        if not self.items:
            print("The inventory is empty.")
        else:
            print("\n--- Current Inventory ---")
            for item, quantity in self.items.items():
                print(f"- {item}: {quantity}")

    def notify_out_of_stock(self):
        """
        Notify the user about items that are out of stock or have zero quantity.

        Out-of-stock items are those with a quantity less than or equal to zero.
        """
        out_of_stock = [item for item, quantity in self.items.items() if quantity <= 0]
        if not out_of_stock:
            print("No items are out of stock.")
        else:
            print("\n--- Out of Stock Items ---")
            for item in out_of_stock:
                print(f"- {item}")


class Order:
    """
    Class to represent an individual order.
    """

    def __init__(self, order_id):
        self.order_id = order_id
        self.items = Counter()
        self.status = OrderStatus.PENDING

    def add_item(self, item_name, quantity):
        """
        Add an item to the order.

        :param item_name: Name of the item to add.
        :param quantity: Quantity of the item to add.
        """
        self.items[item_name] += quantity

    def show_order(self):
        """
        Display the details of the order.
        """
        print(f"\nOrder #{self.order_id}")
        for item, quantity in self.items.items():
            print(f"  - {item}: {quantity}")
        print(f"  Status: {self.status.name}")


class OrderManager:
    """
    Class to manage all orders, including creation and status updates.
    """

    def __init__(self):
        self.orders = {}
        self.next_order_id = 1

    def create_order(self, inventory):
        """
        Create a new order and deduct items from the inventory.

        :param inventory: The Inventory object to check and deduct items.
        """
        order = Order(self.next_order_id)
        while True:
            item_name = input("Enter the item name for the order (or type 'done' to finish): ").strip()
            if item_name.lower() == "done":
                break

            if item_name not in inventory.items or inventory.items[item_name] <= 0:
                print(f"Item '{item_name}' is out of stock or unavailable.")
                continue

            try:
                quantity = int(input(f"Enter the quantity of '{item_name}': ").strip())
                if inventory.remove_item(item_name, quantity):
                    order.add_item(item_name, quantity)
                    print(f"Added {quantity} of '{item_name}' to the order.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        if order.items:
            self.orders[order.order_id] = order
            self.next_order_id += 1
            print(f"Order #{order.order_id} created successfully!")
        else:
            print("No items were added to the order.")

    def show_orders(self):
        """
        Display all orders and their details.
        """
        if not self.orders:
            print("No orders available.")
        else:
            for order in self.orders.values():
                order.show_order()

    def update_order_status(self):
        """
        Update the status of an existing order.
        """
        try:
            order_id = int(input("Enter the order ID to update: ").strip())
            if order_id not in self.orders:
                print(f"Order #{order_id} does not exist.")
                return

            print("Choose a new status:")
            print("1. Pending")
            print("2. Shipped")
            print("3. Delivered")
            status_choice = input("Enter your choice: ").strip()

            order = self.orders[order_id]
            if status_choice == "1":
                order.status = OrderStatus.PENDING
            elif status_choice == "2":
                order.status = OrderStatus.SHIPPED
            elif status_choice == "3":
                order.status = OrderStatus.DELIVERED
            else:
                print("Invalid choice. Status not updated.")
                return
            print(f"Order #{order_id} status updated to {order.status.name}.")
        except ValueError:
            print("Invalid input. Please enter a valid order ID.")


class InventoryManagementSystem:
    """
    Class to manage the overall system, including inventory and orders.
    """

    def __init__(self):
        self.inventory = Inventory()
        self.order_manager = OrderManager()

    def display_menu(self):
        """
        Display the main menu.
        """
        print("\n--- Inventory and Order Management System ---")
        print("1. Add new item to inventory")
        print("2. Create a new order")
        print("3. Show all orders")
        print("4. Update order status")
        print("5. Show inventory")
        print("6. Notify out-of-stock items")
        print("7. Exit")

    def run(self):
        """
        Run the main program loop.
        """
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                item_name = input("Enter the item name: ").strip()
                try:
                    quantity = int(input(f"Enter the quantity of '{item_name}': ").strip())
                    self.inventory.add_item(item_name, quantity)
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
            elif choice == "2":
                self.order_manager.create_order(self.inventory)
            elif choice == "3":
                self.order_manager.show_orders()
            elif choice == "4":
                self.order_manager.update_order_status()
            elif choice == "5":
                self.inventory.show_inventory()
            elif choice == "6":
                self.inventory.notify_out_of_stock()
            elif choice == "7":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")


# Run the system
ims = InventoryManagementSystem()
ims.run()
