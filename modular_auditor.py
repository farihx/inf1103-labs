inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or type 'quit' to stop): ")

    if stock.lower() == "quit":
        break

    if not stock.isdigit():
        print("Error: Please enter a valid non-negative integer.")
        failed_entries += 1
        continue

    stock = int(stock)

    if stock < 0:
        print("Error: Negative stock values are not allowed.")
        failed_entries += 1
        continue

    inventory += stock

    if inventory > 500:
        print("Alert: Inventory has exceeded 500 units!")
        break

    print("Current inventory:", inventory)

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)