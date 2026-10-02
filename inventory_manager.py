import json

# inventory = [
#     {
#         "id": "P001",
#         "name": "Laptop",
#         "price": 1200.00,
#         "stock": 15
#     },
#     {
#         "id": "P002",
#         "name": "Mouse",
#         "price": 25.50,
#         "stock": 40
#     },
#     {
#         "id": "P003",
#         "name": "Keyboard",
#         "price": 45.00,
#         "stock": 25
#     }
# ]

def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    if not inventory:
        print("Inventory is empty.")
        return

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("------------------------------------------------")

def search_product(inventory, product_id):
   for product in inventory:
       if product["id"].lower() == product_id.lower():
           return product

   return None

def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ")

    if search_product(inventory, product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Product Name: ")

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

    except ValueError:
        print("Invalid price or stock quantity.")
        return

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

    print("Product added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    product = search_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print("Name:", product["name"])
    print("Current Stock:", product["stock"])

    try:
        new_stock = int(input("New Stock Quantity: "))

        if new_stock < 0:
            print("Stock cannot be negative.")
            return

    except ValueError:
        print("Invalid stock quantity.")
        return

    product["stock"] = new_stock

    print("Stock updated successfully!")

def search_product_menu(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    product = search_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("------------------------------------------------")
    print("ID:", product["id"])
    print("Name:", product["name"])
    print(f"Price: ${product['price']:.2f}")
    print("Stock:", product["stock"])
    print("------------------------------------------------")

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        return inventory

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with empty inventory.")

        return []

# loaded_inventory = load_inventory()
# display_all(loaded_inventory)

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

print("=" * 40)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 40)

inventory = load_inventory()

while True:
    display_menu()

    option = input("Enter option: ")

    if option == "1":
        display_all(inventory)

    elif option == "2":
        add_product(inventory)

    elif option == "3":
        update_stock(inventory)

    elif option == "4":
        search_product_menu(inventory)

    elif option == "5":
        print("Saving inventory...")
        save_inventory(inventory)

    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please select 1 to 6.")