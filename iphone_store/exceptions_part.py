class InvalidPriceError(Exception):
    """
    If the price for a Product is <= 0, this error would be raised.
    """
    def __init__(self, price: int | float, exception: str):
        super().__init__(exception)
        self.price = price
        self.exception = exception

    def __str__(self):
        return f"Price '{self.price}' is invalid. {self.exception}"

class InvalidQuantityError(Exception):
    """
    If you would try to add less then 1 or "float" product amount to the Cart, this error would be raised.
    """
    def __init__(self, quantity: int, exception: str):
        super().__init__(exception)
        self.quantity = quantity
        self.exception = exception

    def __str__(self):
        return f"Product amount must be an integer. Correct your input '{self.quantity}'."
    
