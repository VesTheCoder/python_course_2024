import random
import discount_part
import logging_part
import product_part
import exceptions_part
import payments_part

class Cart(discount_part.DiscountMixin, logging_part.LoggingMixin):
    """
    Main interaction class where user adds products, gets product info, discount info, total cost and chooses the payment method.
    """
    def __init__(self, title="Temp"):
        logging_part.LoggingMixin.__init__(self)
        self.user_products = {}
        self.title = title
        self.log_info(f"Cart '{title}' was created.")

    def add_to_cart(self, product: product_part.Product, quantity: int = 1):
        """
        Forms a dictionary with user products and quantities.
        """
        if not isinstance(quantity, int) or quantity < 1:
            self.log_error(f"Attempt of adding of a wrong product amount to the cart.")  
            raise exceptions_part.InvalidQuantityError(f"Can't add less then 1 or half a product to the cart. Correct your input '{quantity}' for '{product.title}'.")          
        if not isinstance(product, product_part.Product):
            self.log_error(f"Attempt of adding of a product in a wrong format to the cart.")
            raise TypeError(f"Product must be an instance of the Product class.")
        self.user_products[product] = self.user_products.get(product, 0) + quantity
        self.log_info(f"Product '{product.title}' - {quantity} pce(s) was added to the cart.")

    def total_cost(self):
        """
        Calculates and returns a base total cost of user cart.
        """
        self.log_info(f"Total cost of the cart was calculated.")
        return sum(product.price * quantity for product, quantity in self.user_products.items())
    
    def apply_discount(self, total_cost=None):
        """
        Applies a discount to the total cost of the cart, logs the discount, and returns the final price
        with the discount info.
        """
        if total_cost is None:
            total_cost = self.total_cost()
        self.discount = random.choice([discount_part.Discount_Percent(random.randint(1, 95)), discount_part.Discount_Fixed(random.randint(10, 350))])
        final_price = self.discount.apply(total_cost)
        
        if isinstance(self.discount, discount_part.Discount_Percent):
            discount_info = f"{self.discount.discount_percent}%"
        elif isinstance(self.discount, discount_part.Discount_Fixed):
            discount_info = f"${self.discount.discount_amount:.2f}"
        
        self.log_info(f"Discount of {discount_info} was applied. Final cart price: ${final_price:.2f}")
        return final_price, discount_info

    def pay(self, payment_processor: payments_part.PaymentProcessor):
        """
        Calls PaymentProcessor.pay() method to print a message with a payment info.
        """
        payment_process = payment_processor.pay()
        self.log_info(f"User chose his payment method and is ready to pay.")
        return payment_process
    
    def __add__(self, other):
        """
        Combines the content of two carts using the `+` operator. 
        Returns a new Cart containing products from both carts combined.
        """
        if not isinstance(other, Cart):
            return NotImplemented
        
        combined_cart = Cart("Combined cart")
        combined_cart.user_products = self.user_products.copy()

        for product, quantity in other.user_products.items():
            combined_cart.user_products[product] = combined_cart.user_products.get(product, 0) + quantity
        
        self.log_info(f"New cart '{combined_cart.title}' created by adding '{self.title}' and '{other.title}'.")
        return combined_cart

    def __iadd__(self, other):
        """
        Combines the content of two carts in-place using the `+=` operator.
        Modifies the current Cart by adding products from another Cart.
        """
        if not isinstance(other, Cart):
            return NotImplemented
        
        for product, quantity in other.user_products.items():
            self.user_products[product] = self.user_products.get(product, 0) + quantity
        
        self.log_info(f"Cart '{self.title}' was updated by adding '{other.title}'.")
        return self
    
    def __len__(self):
        """
        Returns the number of a separate products in the cart.
        """
        return len(self.user_products)

    def __getitem__(self, index):
        """
        Enables indexed access to the cart's items and slicing.
        """
        if isinstance(index, int):
            items = list(self.user_products.items())
            if index < 0 or index >= len(items):
                raise IndexError("Cart index out of range")
            return items[index]
            
        elif isinstance(index, slice):
            items = list(self.user_products.items())[index]
            return "\n".join([f"{product.title}: {quantity} pce(s) - ${product.price:.2f}" for product, quantity in items])
        else:
            raise TypeError("Cart index must be int or slice")
        
    def __iter__(self):
        """
        Creates the iterator and returns the iterator object - the list of items in the cart.
        """
        self._iteration_index = 0
        self._user_items = list(self.user_products.items())
        return self

    def __next__(self):
        """
        Returns the next item from the user cart. When all items are iterated, raises StopIteration.
        """
        if self._iteration_index < len(self._cart_items):
            item = self._user_items[self._iteration_index]
            self._iteration_index += 1
            return item
        else:
            raise StopIteration
        
    def __str__(self):
        """
        Forms a final content of the user cart info (without discount) and returns it in str format.
        """
        user_cart = [f"\nHere's your cart:\n"]
        for product, quantity in self.user_products.items():
            user_cart.append(f"{product} - {quantity} pce(s)\n")
        user_cart.append(f"Total cost: ${self.total_cost():.2f}\n")
        self.log_info(f"User cart info was formed and the user was informed about it's content.")
        return "".join(user_cart)