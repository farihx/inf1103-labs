from product import Product


class Inventory:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")

        if self.find_product(product.product_id) is not None:
            raise ValueError("A product with this ID already exists.")

        self.products.append(product)

    def remove_product(self, product_id: str) -> Product | None:
        product = self.find_product(product_id)

        if product is not None:
            self.products.remove(product)

        return product

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    def display_all_products(self) -> None:
        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            product.display_information()
            print(product.get_fulfilment_info())
            print("-" * 40)

    def get_products(self) -> list[Product]:
        return self.products.copy()

    # Retain these aliases for compatibility with the Lab 7 manager.

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def display_all(self) -> None:
        self.display_all_products()