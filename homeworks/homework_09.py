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
# Реалізуйте програму, яка виведе наступний член послідовності на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. 
def func_detect(seq):
    """
    Detects the type of sequence and goes to the fitting function.
    """
    if all(seq[i + 1] - seq[i] == seq[1] - seq[0] for i in range(1, len(seq)-1)):
        return func_arithmetic(seq)    
    if all(seq[i + 1] / seq[i] == seq[1] / seq[0] for i in range(1, len(seq)-1)):
        return func_geometric(seq)
    if all(round(seq[i] ** 0.5) ** 2 == seq[i] for i in range(1, len(seq))):
        return func_square(seq)
    if all(round(seq[i] ** (1/3)) ** 3 == seq[i] for i in range(1, len(seq))):
        return func_cube(seq) 
    if len(seq) >= 4 and seq[0] + seq[1] == seq[-1] + seq[-2]:
        return func_recurring(seq)
    return ("hella knows what, ANYWAY", seq[-1] + (seq[-1] - seq[-2]))

def func_arithmetic(seq):
    """
    Detects the next element of the arithmetic sequence.
    """
    diff = seq[1] - seq[0]
    return ("arithmetic", seq[-1] + diff)

def func_geometric(seq):
    """
    Detects the next element of the geometric sequence.
    """
    diff = int(seq[1] / seq[0])
    return ("geometric", seq[-1] * diff)

def func_square(seq):
    """
    Detects the next element of the square sequence.
    """
    num = int(seq[-1]**0.5)
    return ("square", (num + 1) ** 2)

def func_cube(seq):
    """
    Detects the next element of the cube sequence.
    """
    num = int(seq[-1]**(1/3))
    return ("cubic", (num + 1) ** 3)

def func_recurring(seq):
    """
    Detects the next element of the recurring sequence.
    """
    length = len(seq)
    for i in range(1, length // 2 + 1):
        if seq[:i] == seq[i:2*i]:
            return ("recurring", seq[length % i])

def main():
    user_input = input("Give me your sequense separated by comma (ex. 0,2,4,6): ").strip().replace(" ", "").split(",")
    sequence = [int(x) for x in user_input]
    if len(sequence) < 2:
        print("Sorry not sorry, at least 2 elements are required. Bye!")
    else:
        next_element = func_detect(sequence)
        print(f"Your sequence is {next_element[0]}! {next_element[1]} goes next. It's {', '.join(map(str, sequence))}, {next_element[1]}.")

if __name__ == "__main__":
    main()

# Task 5
# Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат.
ONES = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
ELEVENS = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
TWENTIES = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
THOUSANDS = {1: "thousand", 2: "million", 3: "billion", 4: "trillion", 5: "quadrillion", 6: "quintillion", 7: "sextillion", 
             8: "septillion", 9: "octillion", 10: "nonillion", 11: "decillion"}
def func_spelling(part):
    if part == 0:
        return ""
    if part < 10:
        return ONES[part] + " "
    if part < 20:
        return ELEVENS[part] + " "
    if part < 100:
        return TWENTIES[part // 10 * 10]  + " " + ONES[part % 10] + " "
    if part < 1000:
        return ONES[part // 100] + " hundred " + func_spelling(part % 100)
    for key, value in THOUSANDS.items():
        if part < 1000 ** (key + 1):
            return func_spelling(part // 1000 ** key) + value + " " + func_spelling(part % 1000 ** key)

def func_dollars(*ints):
    return (func_spelling(dollars) + ("dollar" if dollars == 1 else "dollars")).capitalize()

def func_cents(*ints):
    return " and " + func_spelling(cents) + ("cent" if cents == 1 else "cents") if cents else ""

user_input = input("Input the amount of $$$ to know how to spell it correctly (ex. 145.10): ").strip().replace(",", ".").split(".")
dollars = int(user_input[0])
cents = int(user_input[1].ljust(2, "0")[:2]) if len(user_input) > 1 else 0
print(f"This number is spelled as '{func_dollars(dollars) + func_cents(cents)}'")
