import logging
import random

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

class LoggingMixin:
    """
    Service mixin class to write logs into file.
    """
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(f"logs_{self.__class__.__name__}.log")
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_debug(self, message: str):
        self.logger.debug(message)

    def log_info(self, message: str):
        self.logger.info(message)

    def log_warning(self, message: str):
        self.logger.warning(message)

    def log_error(self, message: str):
        self.logger.error(message)

    def log_critical(self, message: str):
        self.logger.critical(message)

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
            raise InvalidPriceError(f"The product price must be positive, correct your input '{price}' for '{title}'.")
        self.title = title
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.title} (${self.price}) - {self.description}"

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

class PaymentProcessor:
    """
    Base payment processor class, has to be overridden in subclasses.
    """
    def pay(self):
        return NotImplementedError

class CC_Processor(PaymentProcessor):
    """
    Class to process credit card payments.
    """
    def __init__(self, credit_card_number: str, expiration_date: str, cvv: str):
        self.cc_number = credit_card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def pay(self):
        """
        Prints a message with an info about the payment, if user payment method is credit card. 
        """
        return f"\nCard number: {self.cc_number[0:4]}****{self.cc_number[-4:]}. Please approve the payment. Thank you!"

class PayPal_Processor(PaymentProcessor):
    """
    Class to process PayPal payments.
    """
    def __init__(self, paypal_email: str):
        self.paypal_email = paypal_email
    
    def pay(self):
        """
        Prints a message with an info about the payment, if user payment method is PayPal. 
        """
        return f"\nPlease check your email, we sent you a payment request to {self.paypal_email}. Thank you!"

class BankTransfer_Processor(PaymentProcessor):
    """
    Class to process bank transfer payments.
    """
    def __init__(self, bank_name: str, account_number: str):
        self.bank_name = bank_name
        self.account_number = account_number
    
    def pay(self):
        """
        Prints a message with an info about the payment, if user payment method is bank transfer. 
        """
        return f"\nPlease check your bank app, we sent you a payment request to the account {self.account_number}. Thank you!"

class DiscountMixin:
    """
    Service mixin class to apply discounts to user carts.
    """
    def apply_discount(self, discount: Discount):
        total_amount = self.total_cost()
        return discount.apply(total_amount)

class Cart(DiscountMixin, LoggingMixin):
    """
    Main interaction class where user adds products, gets product info, discount info, total cost and chooses the payment method.
    """
    def __init__(self, title="Temp"):
        LoggingMixin.__init__(self)
        self.user_products = {}
        self.title = title
        self.log_info(f"Cart '{title}' was created.")

    def add_to_cart(self, product: Product, quantity: int = 1):
        """
        Forms a dictionary with user products and quantities.
        """
        if not isinstance(quantity, int) or quantity < 1:
            self.log_error(f"Attempt of adding of a wrong product amount to the cart.")  
            raise InvalidQuantityError(f"Can't add less then 1 or half a product to the cart. Correct your input '{quantity}' for '{product.title}'.")          
        if not isinstance(product, Product):
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
        self.discount = random.choice([Discount_Percent(random.randint(1, 95)), Discount_Fixed(random.randint(10, 350))])
        total_cost = self.total_cost()
        final_price = self.discount.apply(total_cost)
        
        if isinstance(self.discount, Discount_Percent):
            discount_info = f"{self.discount.discount_percent}%"
        elif isinstance(self.discount, Discount_Fixed):
            discount_info = f"${self.discount.discount_amount:.2f}"
        
        self.log_info(f"Discount of {discount_info} was applied. Final cart price: ${final_price:.2f}")
        return final_price, discount_info

    def pay(self, payment_processor: PaymentProcessor):
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
    add_product_1 = Product("IDIOT PHONE", 696969, "Dafuq is that")
    dic_products["IDIOT PHONE"] = add_product_1
except (TypeError, InvalidPriceError) as exception:
    print(exception)

user_cart = Cart("Cart_1")
print(f"WE SELL IPHONES!!!\n")

final_choice = "bim bim bam bam"
while final_choice != "n":
    while True:
        try:
            what_iphone = input("What iPhone do you want to buy? ").strip().upper()
            if what_iphone not in dic_products:
                raise KeyError 
            break  
        except KeyError:
            print("Sorry, we don't have this model, buy something better.") 
            continue 

    while True:
        try: 
            what_quantity = int(input("How many do you want? (1, 2, 3, etc.) ").strip())
            if what_quantity < 1:
                raise ValueError
            user_cart.add_to_cart(dic_products[what_iphone], what_quantity)
            break
        except ValueError:
            print("You can't buy less then one or half an iPhone, please repeat your input.")
            continue   
    final_choice = input("Great! Do you want to add more to your cart? (y/n) ").lower().strip()

total_cost = user_cart.total_cost()
final_price, discount_info = user_cart.apply_discount()
print(f"{user_cart}But, You are getting an extra discount of {discount_info}! \nFinal total: ${final_price:.2f}")

payment_method = input(f"What payment method do you want to use? (input 1, 2 or 3) \n1. Credit Card \n2. PayPal \n3. Bank Transfer\n")
while payment_method not in ("1", "2", "3"):
    LoggingMixin.log_error(f"User attempted to use an unexistent payment method.")
    payment_method = input(f"Sorry, wrong input. Please input 1, 2 or 3 \n1. Credit Card \n2. PayPal \n3. Bank Transfer\n")
else:
    if payment_method == "1":
        credit_card_number = input("Please input your credit card number: ")
        expiration_date = input("Please input your expiration date: ")
        cvv = input("Please input your CVV: ")
        payment_details = CC_Processor(credit_card_number, expiration_date, cvv)
    elif payment_method == "2":
        paypal_email = input("Please input your PayPal email: ")
        payment_details = PayPal_Processor(paypal_email)
    else:
        bank_name = input("Please input your bank name: ")
        account_number = input("Please input your account number: ")
        payment_details = BankTransfer_Processor(bank_name, account_number)
print(user_cart.pay(payment_details))