class Discount:
    """
    Base class for discounts, has to be overridden in subclasses.
    """
    def apply(self):
        return NotImplementedError

class Discount_Percent(Discount):
    """
    Class to count percentage discounts.
    """
    def __init__(self, discount_percent: int):
        self.discount_percent = discount_percent
    
    def apply(self, price: int | float):
        return price - (price / 100 * self.discount_percent)

class Discount_Fixed(Discount):
    """
    Class to count fixed $ discounts.
    """
    def __init__(self, discount_amount: int | float):
        self.discount_amount = discount_amount
    
    def apply(self, price: int | float):
        return price - self.discount_amount
    
class DiscountMixin:
    """
    Service mixin class to apply discounts to user carts.
    """
    def apply_discount(self, discount: Discount):
        total_amount = self.total_cost()
        return discount.apply(total_amount)