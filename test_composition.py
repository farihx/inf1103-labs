from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

# Create a Supplier
supplier = Supplier(
    "S001",
    "Tech Supplies Pte Ltd",
    "sales@example.com"
)

# Create two Product objects
physical = PhysicalProduct(
    "P001", "Guitar", 500.00, 10, 3.5, supplier
)

digital = DigitalProduct(
    "D001", "Operating System", 99.00, 50, 450.0, supplier
)

# Create two Orders
order1 = Order("O001")
order2 = Order("O002")

# Add products to Order 1
order1.add_order_line(physical, 2)
order1.add_order_line(digital, 1)

# Add the SAME physical Product to Order 2
order2.add_order_line(physical, 3)

# Display both Orders
print("ORDER 1")
order1.display_order()

print("\nORDER 2")
order2.display_order()

# Check the number of Product and OrderLine objects
print("\nOBJECT RELATIONSHIP TESTS")

print(
    "Number of OrderLine objects:",
    len(order1.order_lines) + len(order2.order_lines)
)

print(
    "OrderLines are separate objects:",
    order1.order_lines[0] is not order2.order_lines[0]
)

print(
    "Both OrderLines reference the same Product:",
    order1.order_lines[0].product is order2.order_lines[0].product
)

# Remove an OrderLine through its owning Order
removed_line = order1.remove_order_line(0)

print("\nAfter removing the first OrderLine from Order 1:")
order1.display_order()

print("\nOriginal Product still exists:")
physical.display_information()