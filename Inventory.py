class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}  # Dictionary to store inventory items
        self.sales = 0  # Variable to track total sales

    def add_item(self, item_name, price, quantity):
        """Add an item to the inventory with name, price, and quantity."""
        if item_name in self.inventory:
            print(f"{item_name} already exists. Use update_item to change stock.")
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}
            print(f"Added {item_name} to the inventory.")

    def update_item(self, item_name, price=None, quantity=None):
        """Update price or quantity of an existing item."""
        if item_name in self.inventory:
            if price is not None:
                self.inventory[item_name]['price'] = price
            if quantity is not None:
                self.inventory[item_name]['quantity'] += quantity
            print(f"Updated {item_name}.")
        else:
            print(f"{item_name} does not exist in the inventory.")

    def remove_item(self, item_name):
        """Remove an item from the inventory."""
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Removed {item_name} from the inventory.")
        else:
            print(f"{item_name} not found in the inventory.")

    def purchase_item(self, item_name, quantity):
        """Process the purchase of an item and adjust stock."""
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] >= quantity:
                self.inventory[item_name]['quantity'] -= quantity
                total_price = self.inventory[item_name]['price'] * quantity
                self.sales += total_price
                print(f"Purchased {quantity} of {item_name}. Total: ${total_price}")
            else:
                print(f"Insufficient stock of {item_name}.")
        else:
            print(f"{item_name} not found in inventory.")

    def view_inventory(self):
        """Display the current inventory."""
        print("Inventory:")
        for item_name, details in self.inventory.items():
            print(f"{item_name} - Price: ${details['price']}, Quantity: {details['quantity']}")

    def view_sales(self):
        """Display total sales made."""
        print(f"Total Sales: ${self.sales}")

def main():
    system = InventoryManagementSystem()
    
    while True:
        print("\nInventory Management System:")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Purchase Item")
        print("6. View Total Sales")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            system.add_item(item_name, price, quantity)

        elif choice == '2':
            item_name = input("Enter item name to update: ")
            price = input("Enter new price (leave blank to skip): ")
            quantity = input("Enter quantity to add (leave blank to skip): ")
            price = float(price) if price else None
            quantity = int(quantity) if quantity else None
            system.update_item(item_name, price, quantity)

        elif choice == '3':
            item_name = input("Enter item name to remove: ")
            system.remove_item(item_name)

        elif choice == '4':
            system.view_inventory()

        elif choice == '5':
            item_name = input("Enter item name to purchase: ")
            quantity = int(input("Enter quantity to purchase: "))
            system.purchase_item(item_name, quantity)

        elif choice == '6':
            system.view_sales()

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
