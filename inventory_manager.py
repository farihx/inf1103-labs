import json
from product import Product
from inventory import Inventory

# Load inventory data from JSON
def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                float(item["price"]),
                int(item["stock"])
            )

            inventory.add_product(product)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with empty inventory.")

    return inventory


# Save inventory data to JSON
def save_inventory(inventory):
    data = []

    for product in inventory.get_products():
        product_data = {
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }

        data.append(product_data)

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


# Add a new product
def add_product_menu(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip()

    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

        product = Product(product_id, name, price, stock)
        inventory.add_product(product)

        print("Product added successfully!")

    except ValueError as error:
        print("Invalid product details:", error)


# Update an existing product's stock
def update_stock_menu(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    product.display_information()

    try:
        new_stock = int(input("New Stock Quantity: "))

        if new_stock < 0:
            print("Stock cannot be negative.")
            return

        product.update_stock(new_stock)

        print("Stock updated successfully!")

    except ValueError as error:
        print("Invalid stock quantity:", error)


# Search for a product
def search_product_menu(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nProduct Found")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")


# Display the menu
def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# Main programme
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        display_menu()

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product_menu(inventory)

        elif option == "3":
            update_stock_menu(inventory)

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


if __name__ == "__main__":
    main()