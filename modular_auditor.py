def get_valid_input():
    stock = input("Enter stock quantity (or type 'quit' to stop): ")

    if stock.lower() == "quit":
        return "quit"

    if not stock.isdigit():
        print("Error: Please enter a valid non-negative integer.")
        return None

    return int(stock)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)
    tax = calculate_tax(stock)
    deliveries_processed += 1

    print("Tax for this delivery:", tax)

    if inventory > 500:
        print("Alert: Inventory has exceeded 500 units!")
        break

    print("Current inventory:", inventory)

generate_report(inventory, failed_entries)