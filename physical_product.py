from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float
    ):
        super().__init__(product_id, name, price, stock)

        if weight < 0:
            raise ValueError("Weight cannot be negative.")

        self.__weight = float(weight)

    @property
    def weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return round(5.00 + (self.__weight * 2.00), 2)