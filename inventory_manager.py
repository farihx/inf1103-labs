import json

from inventory import Inventory
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped


INVENTORY_FILE = "inventory.json"


def load_inventory() -> Inventory:
    inventory = Inventory()
    supplier_cache: dict[str, Supplier] = {}

    try:
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")
        return inventory

    except json.JSONDecodeError:
        print("Inventory file contains invalid JSON.")
        return inventory

    for item in data:
        supplier_data = item.get("supplier", {})

        supplier_id = supplier_data.get("supplier_id", "S001")

        # Reuse an existing Supplier object if its ID is already loaded.
        if supplier_id in supplier_cache:
            supplier = supplier_cache[supplier_id]

        else:
            supplier = Supplier(
                supplier_id,
                supplier_data.get("name", "Default Supplier"),
                supplier_data.get(
                    "contact_email",
                    "unknown@example.com"
                )
            )

            supplier_cache[supplier_id] = supplier

        product_type = item.get("type", "physical")

        if product_type == "physical":
            product = PhysicalProduct(
                item["id"],
                item["name"],
                float(item["price"]),
                int(item["stock"]),
                float(item["weight"]),
                supplier
            )

        elif product_type == "digital":
            product = DigitalProduct(
                item["id"],
                item["name"],
                float(item["price"]),
                int(item["stock"]),
                float(item["download_size"]),
                supplier
            )

        else:
            raise ValueError(
                f"Unknown product type: {product_type}"
            )

        inventory.add_product(product)

    return inventory


def save_inventory(inventory: Inventory) -> None:
    data = []

    for product in inventory.get_products():

        item = {
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "supplier": {
                "supplier_id": product.supplier.supplier_id,
                "name": product.supplier.name,
                "contact_email": product.supplier.contact_email
            }
        }

        if isinstance(product, PhysicalProduct):
            item["type"] = "physical"
            item["weight"] = product.weight

        elif isinstance(product, DigitalProduct):
            item["type"] = "digital"
            item["download_size"] = product.download_size

        else:
            raise TypeError("Unsupported product type.")

        data.append(item)

    with open(INVENTORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def get_or_create_supplier(inventory: Inventory) -> Supplier:
    supplier_id = input("Enter Supplier ID: ").strip()

    # Reuse a Supplier object already associated with an existing Product.
    for product in inventory.get_products():
        if product.supplier.supplier_id == supplier_id:
            print("Existing supplier found. Reusing supplier information.")
            return product.supplier

    # Create a new Supplier if the ID does not already exist.
    name = input("Enter Supplier Name: ").strip()
    contact_email = input("Enter Supplier Email: ").strip()

    return Supplier(supplier_id, name, contact_email)


def add_product_menu(inventory: Inventory) -> None:
    print("\n--- Add Product ---")

    product_id = input("Enter Product ID: ").strip()

    if inventory.find_product(product_id) is not None:
        print("A product with this ID already exists.")
        return

    name = input("Enter Product Name: ").strip()

    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Stock Quantity: "))

    print("\nChoose Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")

    product_choice = input("Enter choice: ").strip()

    if product_choice not in ["1", "2"]:
        print("Invalid product type.")
        return

    supplier = get_or_create_supplier(inventory)

    if product_choice == "1":
        weight = float(input("Enter Weight (kg): "))

        product = PhysicalProduct(
            product_id,
            name,
            price,
            stock,
            weight,
            supplier
        )

    else:
        download_size = float(
            input("Enter Download Size (MB): ")
        )

        product = DigitalProduct(
            product_id,
            name,
            price,
            stock,
            download_size,
            supplier
        )

    inventory.add_product(product)

    print("Product added successfully.")


def update_stock_menu(inventory: Inventory) -> None:
    print("\n--- Update Stock ---")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print(f"Current Stock: {product.stock}")

    new_stock = int(input("Enter New Stock Quantity: "))

    product.update_stock(new_stock)

    print("Stock updated successfully.")


def search_product_menu(inventory: Inventory) -> None:
    print("\n--- Search Product ---")

    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    product.display_information()

    print(product.get_fulfilment_info())

    if isinstance(product, CanBeShipped):
        print(
            f"Shipping Cost: "
            f"${product.calculate_shipping_cost():.2f}"
        )


def display_menu() -> None:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Update Stock")
    print("3. Search Product")
    print("4. Display All Products")
    print("5. Exit")


def main() -> None:
    inventory = load_inventory()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_product_menu(inventory)
                save_inventory(inventory)

            elif choice == "2":
                update_stock_menu(inventory)
                save_inventory(inventory)

            elif choice == "3":
                search_product_menu(inventory)

            elif choice == "4":
                inventory.display_all_products()

            elif choice == "5":
                save_inventory(inventory)
                print("Inventory saved. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except (ValueError, TypeError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()