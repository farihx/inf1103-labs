from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# Create a Supplier
supplier = Supplier(
    "S001",
    "Tech Supplies Pte Ltd",
    "sales@example.com"
)

# Create both Product subclasses
physical = PhysicalProduct(
    "P001", "Guitar", 500.00, 10, 3.5, supplier
)

digital = DigitalProduct(
    "D001", "Operating System", 99.00, 50, 450.0, supplier
)

# Test the same function with both subclasses
print("PHYSICAL PRODUCT DETAILS")
show_product_details(physical)

print("\nDIGITAL PRODUCT DETAILS")
show_product_details(digital)

# Add both types to the same Inventory
inventory = Inventory()

inventory.add_product(physical)
inventory.add_product(digital)

print("\nINVENTORY CONTENTS")
inventory.display_all_products()

# Check inherited Product behaviour
print("\nTESTING INHERITED STOCK UPDATE")

digital.update_stock(40)

print("Updated Digital Product Stock:", digital.stock)