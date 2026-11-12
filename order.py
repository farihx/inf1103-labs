from product import Product
from order_line import OrderLine


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(
        self,
        product: Product,
        quantity: int
    ) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, index: int) -> OrderLine | None:
        if 0 <= index < len(self.order_lines):
            return self.order_lines.pop(index)

        return None

    def calculate_total(self) -> float:
        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total

    def display_order(self) -> None:
        print(f"Order ID: {self.order_id}")

        if not self.order_lines:
            print("This order has no items.")
            return

        for index, order_line in enumerate(self.order_lines, start=1):
            print(
                f"{index}. {order_line.product.name} | "
                f"Quantity: {order_line.quantity} | "
                f"Subtotal: ${order_line.calculate_subtotal():.2f}"
            )

        print(f"Order Total: ${self.calculate_total():.2f}")