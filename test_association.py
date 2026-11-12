from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# Create a Supplier object
supplier = Supplier(
    "S001",
    "Tech Supplies Pte Ltd",
    "sales@example.com"
)

# Create products using the same Supplier object
physical = PhysicalProduct(
    "P001", "Laptop", 1200.00, 15, 1.5, supplier
)

digital = DigitalProduct(
    "D001", "Operating System", 99.00, 50, 450.0, supplier
)

# Confirm that both products refer to the same Supplier object
print("Physical and digital share the same supplier:")
print(physical.supplier is digital.supplier)

# Delete the original variable
del supplier

# Display supplier information through each Product
print("\nPHYSICAL PRODUCT")
physical.display_information()

print("\nDIGITAL PRODUCT")
digital.display_information()