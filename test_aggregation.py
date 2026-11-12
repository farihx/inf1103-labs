from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

# Create a Supplier and Product first
supplier = Supplier(
    "S001",
    "Tech Supplies Pte Ltd",
    "sales@example.com"
)

product = PhysicalProduct(
    "P001", "Laptop", 1200.00, 15, 1.5, supplier
)

# Create two inventories
inventory_a = Inventory()
inventory_b = Inventory()

# Add the existing Product to Inventory A
inventory_a.add_product(product)

print("Product in Inventory A:")
print(inventory_a.find_product("P001") is product)

# Remove the Product from Inventory A
removed_product = inventory_a.remove_product("P001")

print("\nProduct successfully removed:")
print(removed_product is product)

# Confirm the Product still exists and works
print("\nProduct still exists:")
print(product.name)

product.display_information()

# Add the SAME Product object to Inventory B
inventory_b.add_product(product)

print("\nProduct in Inventory B:")
print(inventory_b.find_product("P001") is product)

print("\nInventory A:")
inventory_a.display_all_products()

print("\nInventory B:")
inventory_b.display_all_products()