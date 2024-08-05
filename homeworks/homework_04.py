#Task 1
#Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
#Примітка: щасливим квитком називається число, у якому, при парній кількості цифр, сума цифр його лівої половини дорівнює сумі цифр його правої половини.
#Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.
#Answer 1
user_number = input("If your another number is lucky, you get the prize! Input any 4-digit number here: ")
if len(user_number) != 4:
    print("Sorry, that's not a 4-digit numbur. GERARA HERE MAN")
else:
    digits = [int(dig) for dig in user_number]
    lott_res = "Gratz, your number is a lucky one, get your prize!" if sum(digits[:2]) == sum(digits[2:]) else "Sorry, not a lucky number, no prize for you"
    print(lott_res)

#Task 2
#З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
#Примітка: Паліндром називається число, слово або текст, які однаково читаються зліва направо і справа наліво.
#Наприклад, це числа 143341, 5555, 7117 і т.д.
user_number2 = input("Come up with any number. Would it be a palindrome? Input any number here: ")
digits2 = [int(dig) for dig in user_number2]
res_pali = "That's a palindrome number, WOW!" if digits2 == digits2[::-1] else "That's  not a palindrome number, you suck."
print(res_pali)

#Task 3
#Дано коло з центром на початку координат та радіусом 4. Користувач вводить з клавіатури координати точки x та y. 
#Написати програму, яка визначить, лежить ця точка всередині кола чи ні.
print("The center of the circle is at the start of coordinate axis, it's radius is 4. Let's see if your dot would be inside of the circle")
circle_radius = 4
dot_x = float(input("Input x-coordinate for your dot: "))
dot_y = float(input("Input y-coordinate for your dot: "))
dot_res = "The dot is inside, yey!" if dot_x ** 2 + dot_y ** 2 < circle_radius ** 2 else "The dot is not inside, sad :-("
print(dot_res)
