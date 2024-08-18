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
    
    def apply_discount(self):
        """
        Applies a discount to the total cost of the cart, logs the discount, and returns the final price
        with the discount info.
        """
        self.discount = random.choice([discount_part.Discount_Percent(random.randint(1, 95)), discount_part.Discount_Fixed(random.randint(10, 350))])
        total_cost = self.total_cost()
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