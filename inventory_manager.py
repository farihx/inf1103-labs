import json

inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]

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

loaded_inventory = load_inventory()
display_all(loaded_inventory)