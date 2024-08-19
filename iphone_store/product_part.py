import exceptions_part

class Product:
    """
    Class for adding products available in the store.
    """
    def __init__(self, title: str, price: int | float, description: str):
        super().__init__()
        if not isinstance(price, int | float):
            self.log_info(f"Attempt of adding of a wrong product price to the store.")
            raise TypeError(f"The product price must be a number, correct price for '{title}'.")
        if price <= 0:
            self.log_info(f"Attempt of adding of a wrong product price to the store.")
            raise exceptions_part.InvalidPriceError(f"The product price must be positive, correct your input '{price}' for '{title}'.")
        self.title = title
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.title} (${self.price}) - {self.description}"
    
dic_products = {
    "IPHONE 15 PRO MAX": Product("IPHONE 15 PRO MAX", 2000, "Super top-notch"),
    "IPHONE 14 PRO MAX": Product("IPHONE 14 PRO MAX", 1700, "A bit old, but super top-notch"),
    "IPHONE 15 PRO": Product("IPHONE 15 PRO", 1600, "A small top-notch"),
    "IPHONE 14 PRO": Product("IPHONE 14 PRO", 1400, "A bit old, but still small top-notch"),
    "IPHONE 15": Product("IPHONE 15", 1000, "Model for poor people"),
    "IPHONE 14": Product("IPHONE 14", 800, "Old model for very poor people"),
    "IPHONE SE": Product("IPHONE SE", 700, "Cheap version for kids"),
}

try:
    add_product_1 = Product("IDIOT PHONE", 6969, "Dafuq is that")
    dic_products["IDIOT PHONE"] = add_product_1
except (TypeError, exceptions_part.InvalidPriceError) as exception:
    print(exception)
