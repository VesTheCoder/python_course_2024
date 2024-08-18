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