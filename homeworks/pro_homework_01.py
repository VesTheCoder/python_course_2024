import random
class Product:
    """
    Class for adding products available in the store.
    """
    def __init__(self, title: str, price: int | float, description: str):
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
        pass

class Discount_Percent(Discount):
    """
    Class to count percentage discounts.
    """
    def __init__(self, discount_percent: int):
        self.discount_percent = discount_percent
    
    def apply(self, price: int | float):
        return price - (price / 100 * self.discount_percent), f"{self.discount_percent}%"

class Discount_Fixed(Discount):
    """
    Class to count fixed discounts.
    """
    def __init__(self, discount_amount: int | float):
        self.discount_amount = discount_amount
    
    def apply(self, price: int | float):
        return price - self.discount_amount, f"${self.discount_amount:.2f}"

class PaymentProcessor:
    """
    Base payment processor class, has to be overridden in subclasses.
    """
    def pay(self):
        pass

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
    def apply_discount(self, discount):
        total_amount = self.total_cost()
        return discount.apply(total_amount)

class Cart(DiscountMixin):
    """
    Main interaction class where user adds products, gets product info, discount info, total cost and chooses the payment method.
    """
    def __init__(self, title="Temp"):
        self.user_products = {}
        self.title = title

    def add_to_cart(self, product: Product, quantity: int = 1):
        """
        Forms a dictionary with user products and quantities.
        """
        if product in self.user_products:
            self.user_products[product] += quantity
        else:
            self.user_products[product] = quantity

    def total_cost(self):
        """
        Calculates and returns a total cost of user cart.
        """
        return sum(product.price * quantity for product, quantity in self.user_products.items())

    def pay(self, payment_processor: PaymentProcessor):
        """
        Calls PaymentProcessor.pay() method to print a message with a payment info.
        """
        return payment_processor.pay()
        
    def __str__(self):
        """
        Forms a final content of the user cart info (without discount) and returns it in str format.
        """
        user_cart = [f"\nHere's your cart:\n"]
        for product, quantity in self.user_products.items():
            user_cart.append(f"{product} - {quantity} pce(s)\n")
        user_cart.append(f"Total cost: ${self.total_cost():.2f}\n")
        return "".join(user_cart)

dic_products = {
    "IPHONE 15 PRO MAX": Product("IPHONE 15 PRO MAX", 2000, "Super top-notch"),
    "IPHONE 14 PRO MAX": Product("IPHONE 14 PRO MAX", 1700, "A bit old, but super top-notch"),
    "IPHONE 15 PRO": Product("IPHONE 15 PRO", 1600, "A small top-notch"),
    "IPHONE 14 PRO": Product("IPHONE 14 PRO", 1400, "A bit old, but still small top-notch"),
    "IPHONE 15": Product("IPHONE 15", 1000, "Model for poor people"),
    "IPHONE 14": Product("IPHONE 14", 800, "Old model for very poor people"),
    "IPHONE SE": Product("IPHONE SE", 700, "Cheap version for kids")
}

user_cart = Cart("Cart_1")
print(f"WE SELL IPHONES!!!\n")
final_choice = "bim bim bam bam"
while final_choice != "n":
    what_iphone = input("What iPhone do you want to buy? ").strip().upper()
    if what_iphone in dic_products:
        what_quantity = int(input("How many do you want?(1, 2, 3, etc.) ").strip())
        user_cart.add_to_cart(dic_products[what_iphone], what_quantity)
    else:
        print("Sorry, we don't have this model, buy something better.")
    final_choice = input("Do you want to add more to your cart? (y/n) ").lower().strip()

total_cost = user_cart.total_cost()
user_cart.discount = random.choice([Discount_Percent(random.randint(1, 90)), Discount_Fixed(random.randint(10, 350))])
final_price, discount_info = user_cart.apply_discount(user_cart.discount)
print(f"{user_cart}But, You are getting an extra discount of {discount_info}! \nFinal total: ${final_price:.2f}")

payment_method = input(f"What payment method do you want to use? (input 1, 2 or 3) \n1. Credit Card \n2. PayPal \n3. Bank Transfer\n")
while payment_method not in ("1", "2", "3"):
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