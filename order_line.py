from product import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Order quantity must be greater than zero.")

        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return float(self.product.price * self.quantity)