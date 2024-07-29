# Task 1
# Напишіть функцію, яка приймає суму доходу користувача і податкову ставку у відсотках, 
# а повертає розраховану суму податку, яку потрібно сплатити.
def func_calc_tax(user_income, tax):
    return user_income * tax / 100
print("I'll count the amount of your tax.")
user_income_1 = float(input("How much $$$ did you earned? (Input here): "))
tax_1 = float(input("What is the robery rate (%) in your country? (Input here): "))
print(f"\nYou would have to pay ${func_calc_tax(user_income_1, tax_1):.2f} of tax. \nLeave the country asap.")

# Task 2
# Створіть функцію, яка генерує пароль заданої довжини. Функція повинна приймати довжину паролю та булевий параметр, 
# який визначає, чи має пароль містити спеціальні символи (наприклад, @, #, $ тощо).
import string
import random
def func_pass(length, special=False):
    user_pass = string.digits + string.ascii_letters
    if special:
        user_pass += string.punctuation
    return "".join(random.sample(user_pass, length))
print("Let's create a strong password for you!")
length_2 = int(input("What length would you choose? Input: "))
special_2 = input("Do you want to add special characters? Input only 'Yes' or 'No': ").strip().upper() == "YES"
if not special_2:
    print("Got it, no special characters for you")
user_pass_2 = func_pass(length_2, special_2)
print(f"\nYour fresh random password:\n{user_pass_2}")

# Task 3
# Число-паліндром з обох сторін (справа на ліво і зліво на право) читається однаково.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, множенням яких чисел він є.

# Усложнил задачу, чтоб пользователь мог сам задать желаемое максимальное число.
def func_palindrom(user_num):
    for num1 in range(user_num, 1, -1):
        for num2 in range(num1, 1, -1):
            result = num1 * num2
            if str(result) == str(result)[::-1]:
                return (num1, num2, result)
user_num_3 = int(input("Input any number to calculate the biggest palindrom off of: "))
palindrom_3 = func_palindrom(user_num_3)
print(f"The biggest palindrom would be {palindrom_3[2]}.\n A multiplication of {palindrom_3[0]} and {palindrom_3[1]}")

# Task 4
# Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. 
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.


# Task 5
# Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents