
class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        if not product_id.strip():
            raise ValueError("Product ID cannot be empty.")

        if not name.strip():
            raise ValueError("Product name cannot be empty.")

        if price < 0 or stock < 0:
            raise ValueError("Price and stock cannot be negative.")

        self.__product_id = product_id.strip()
        self.__name = name.strip()
        self.__price = float(price)
        self.__stock = int(stock)

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity: int):
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self.__stock = int(quantity)

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )