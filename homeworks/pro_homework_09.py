# Task 1
# Створіть клас "Рахунок", який має приватну властивість "баланс". Використайте дескриптор для реалізації контролю доступу до цієї властивості. 
# Додайте властивість balance з декоратором @property, яка повертає значення балансу. 
# Визначте метод __setattr__, який забороняє безпосереднє змінення значення балансу. 
# Також визначте метод __getattr__, який повертає повідомлення про те, що властивість не існує, якщо доступ до неї спробувати отримати. 
# Використовуйте цей клас для створення об'єкту рахунку та спробуйте змінити значення балансу та отримати доступ до неіснуючої властивості.
class Account:
    """
    This class keeps client's balance info and allows to change it only through special methods, but never directly.
    """
    def __init__(self, balance: int | float):
        super().__setattr__("__balance", balance)

    @property
    def balance(self):
        return f"This client's balance is: {super().__getattribute__('__balance')}"
    
    @balance.setter
    def change_balance(self, value):
        super().__setattr__("__balance", value)

    def __setattr__(self, key, value):
        if key in ("__balance", "balance", "_balance"):
            raise AttributeError("Error: attribute can not be changed.")
        super().__setattr__(key, value)

    def __getattr__(self, key):
        raise AttributeError("Error: Attribute does not exists.")

client_007 = Account(69_420)
print(client_007.balance)
client_007.change_balance = 420_69
print(client_007.balance)

# Task 2
# Створіть клас "Користувач", який має властивості first_name і last_name. 
# Використайте декоратори @property для забезпечення доступу до цих властивостей. 
# Визначте метод __setattr__, який забороняє безпосередню зміну значень first_name і last_name.
# Використовуйте метод __getattr__, який повертає повідомлення про те, що властивість не існує, 
# якщо спробувати отримати доступ до неіснуючої властивості. 
# Створіть об'єкт користувача і спробуйте змінити значення first_name та отримати доступ до неіснуючої властивості.
class User:
    """
    Class for storing user unfo. Allows to change user properties with special methods only.
    """
    def __init__(self, first_name: str, last_name: str):
        super().__setattr__("_first_name", first_name)
        super().__setattr__("_last_name", last_name)

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name
    
    @first_name.setter
    def set_first_name(self, value):
        super().__setattr__("_first_name", value)

    def __setattr__(self, key, value):
        if key in ("first_name", "last_name", "_first_name", "_last_name", "__first_name", "__last_name"):
            raise AttributeError(f"Error: attribute can not be changed.")
        super().__setattr__(key, value)

    def __getattr__(self, key):
        raise AttributeError(f"Error: Attribute does not exists.")

user_01 = User("Vlad", "Ves")
print(user_01.first_name, user_01.last_name)
user_01.set_first_name = "Igor"
print(user_01.first_name, user_01.last_name)
print(user_01.__first_name)

# Task 3
# Створіть клас "Прямокутник", який має приватні властивості width і height. 
# Використайте декоратори @property для створення властивостей width і height, які повертають значення цих властивостей. 
# Визначте метод __setattr__, який забороняє безпосередню зміну значень width і height. 
# Використовуйте метод __getattr__, який повертає повідомлення про те, що властивість не існує, 
# якщо спробувати отримати доступ до неіснуючої властивості. Додайте метод area, який обчислює площу прямокутника. 
# Створіть об'єкт прямокутника і спробуйте змінити значення width і height, 
# а також отримати доступ до неіснуючої властивості та обчислити площу прямокутника.
class Rectangle:
    def __init__(self, width, height):
        super().__setattr__("_width", width)
        super().__setattr__("_height", height)
            
    @property
    def width(self):
        return self._width
    
    @width.setter
    def set_width(self, value):
        super().__setattr__("_width", value)

    @property
    def height(self):
        return self._height
    
    @height.setter
    def set_height(self, value):
        super().__setattr__("_height", value)

    def __setattr__(self, key, value):
        if key in ("width", "height", "_width", "_height", "__width", "__height"):
            raise AttributeError(f"Error: attribute can not be changed.")
        super().__setattr__(key, value)

    def __getattr__(self, key):
        raise AttributeError(f"Error: Attribute does not exists.")
    
    def area(self):
        return self._width * self._height

rectangle = Rectangle(10, 5)
print(f"Width: {rectangle.width}")
print(f"Height: {rectangle.height}")
rectangle.set_width = 15
print(f"Width: {rectangle.width}")
print(f"Area: {rectangle.area()}")