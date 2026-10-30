from product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")

        if self.search_product(product.product_id) is not None:
            raise ValueError("Product ID already exists.")

        self.__products.append(product)

    def search_product(self, product_id: str):
        for product in self.__products:
            if product.product_id.lower() == product_id.strip().lower():
                return product

        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")

        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()

        print("------------------------------------------------")

    def get_products(self):
        return self.__products.copy()