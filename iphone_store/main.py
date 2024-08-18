import exceptions_part
import logging_part
import product_part
import discount_part
import payments_part
import cart_part

if __name__ == "__main__":
    user_cart = cart_part.Cart("Cart_1")
    print(f"\nWE SELL IPHONES!!!\n")

    final_choice = "bim bim bam bam"
    while final_choice != "n":
        while True:
            try:
                what_iphone = input("What iPhone do you want to buy? ").strip().upper()
                if what_iphone not in product_part.dic_products:
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
                user_cart.add_to_cart(product_part.dic_products[what_iphone], what_quantity)
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
        payment_method = input(f"Sorry, wrong input. Please input 1, 2 or 3 \n1. Credit Card \n2. PayPal \n3. Bank Transfer\n")
    else:
        if payment_method == "1":
            credit_card_number = input("Please input your credit card number: ")
            expiration_date = input("Please input your expiration date: ")
            cvv = input("Please input your CVV: ")
            payment_details = payments_part.CC_Processor(credit_card_number, expiration_date, cvv)
        elif payment_method == "2":
            paypal_email = input("Please input your PayPal email: ")
            payment_details = payments_part.PayPal_Processor(paypal_email)
        else:
            bank_name = input("Please input your bank name: ")
            account_number = input("Please input your account number: ")
            payment_details = payments_part.BankTransfer_Processor(bank_name, account_number)
    print(user_cart.pay(payment_details))
