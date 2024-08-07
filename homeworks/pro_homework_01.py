# Cтворіть клас Product для опису товару. У якості атрибутів товару можна використовувати назву, ціну та опис товару. 
# Створіть декілька інстансів класу Product.
# Створіть клас Cart, який буде виступати у якості кошика з товарами певного покупця. Кошик може містити декілька товарів певної кількості. 
# Реалізуйте метод обчислення вартості кошика. В усіх класах має бути визначений метод str.
class Product:
    def __init__(self, title, price, description):
        self.title = title
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.title} (${self.price}) - {self.description}"

class Cart:
    def __init__(self, title="Temp"):
        self.user_products = {}
        self.title = title

    def add_to_cart(self, product, quantity=1):
        if product in self.user_products:
            self.user_products[product] += quantity
        else:
            self.user_products[product] = quantity

    def total_cost(self):
        skoka_deneg = sum(product.price * quantity for product, quantity in self.user_products.items())
        return skoka_deneg

    def __str__(self):
        user_cart = "Here's your cart:\n"
        for product, quantity in self.user_products.items():
            user_cart += f"{product} - {quantity} pce(s) \n"
        user_cart += f"Total price: ${self.total_cost()}\nBuy or get lost."
        return user_cart

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
    final_choice = input("Do you want to buy more? (y/n) ").lower().strip()
print(user_cart)