#Task 1
#Напишіть скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7.
num_1 = 0
num_end = float(input("I will show you all numbers that can be devided by 7 From 0 to (input): "))
list_1 = []
while num_1 < num_end:
    num_1 += 7
    if num_1 < num_end:
        list_1.append(num_1)
print("Here they are")
print(*list_1, sep = ", ")

#Task 2
#Напишіть скрипт для визначення суми цілих непарних чисел від 1 до 99 за допомогою оператора for. Використовуйте цілочисельні змінні summa і count.
sum = 0
for number_2 in range(1, 100, 2):
    sum += number_2
print(f"If we add up all odd numbers from 1 to 99, we get a sum of {sum}")

#Task 3
#Напишіть скрипт, який виводить цілі числа від 1 до 200, використовуючи цикл while. В одному рядку необхідно виведити лише п’ять цілих чисел.
num_3 = 1
count_num_3 = 0
while num_3 <= 200:
    count_num_3 += 1
    print(num_3, end = ' ')
    num_3 += 1
    if count_num_3 == 5:
        print()
        count_num_3 = 0

#Task 4
#Напишіть скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).
num_4 = int(input("Input natural number to count it's factorial: "))
factorial_num_4 = 1
for number_4 in range(1, num_4+1):
    factorial_num_4 *= number_4
print(f"{num_4} factorial equals {factorial_num_4}")

#Task 5
#Напишіть скрипт, який виводить на екран таблицю множення на 5. Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...
print(f"Give me the range to see the multiplication table within this range \nI'll multiply by 5 for you :-*")
range_start = int(input("Range start number would be: "))
range_end = int(input("Range end number would be: "))
if range_start > 0 and range_start <= range_end:
    for num_5 in range(range_start, range_end+1):
        print(f"{num_5} x 5 = {num_5 * 5}")
    print("Here it is, enjoy!")
else:
    print("Sorry, your numbers are idiotic, get lost :-(")

#Task 6
#Напишіть скрипт, який виводить на екран прямокутник із '*'. Висота і ширина прямокутника вводяться з клавіатури.
print("Let me drow a rectangle. Just don't go crazy with the size, ok?")
width = int(input("Define the width (integers only): "))
heith = int(input("Define the heith (integers only): "))
heith_temp = heith
if (width < 2 or width > 50) or (heith < 2 or heith > 50):
    print("Sorry, I wouldn't drow that cause it would look stupid")
else:
    print(f"{'* ' * width}")
    while heith_temp != 2:
        print(f"*{'  ' * (width-2)} *")
        heith_temp -= 1
    print(f"{'* ' * width} \nHERE YOU GO DUDE, THAT'S SICK!!!")

#Task 7
#Є список [0, 5, 2, 4, 7, 1, 3, 19].
#Напишіть скрипт для підрахунку непарних цифр у ньому.
numbers_7 = [0, 5, 2, 4, 7, 1, 3, 19]
odd_numbers = 0
for num_7 in numbers_7:
    if num_7 % 2 != 0:
        odd_numbers += 1
print(*numbers_7, sep = ", ")
print(f"There are {odd_numbers} odd numbers in the given list, hehe")


#Task 8
#Створіть список випадкових чисел (розміром 4 елементи).
#Створіть другий список у два рази більше першого, де перші 4 елементи повинні дорівнювати елементам першого списку, а решта елементів - подвоєним значенням початкових.
import random
list_8 = [random.randint(0, 100) for num8 in range(4)]
double_list_8 = list_8 + [num8 * 2 for num8 in list_8]
print(f"List small {list_8}")
print(f"List big pp {double_list_8}")

#Task 9
#Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць. Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.
print("Let's see your avarage compensation. Input your monthly compensation for the whole year, month by month.")
sal_list_9 = []
mo = 1
while len(sal_list_9) < 12:
    sal = float(input(f"Input what $$$ you've earned in month {mo}: "))
    mo += 1
    if sal > 0:
        sal_list_9.append(sal)
    else:
        print("Compensation can not be less the 0, try harder")
        mo -= 1
print(f"Your list month by month: {sal_list_9}")
print(f"Your avarage yearly compensation was ${sum(sal_list_9) / len(sal_list_9):.2f}")

#Task 10
#Є матриця
#[1, 2, 3, 4]
#[5, 6, 7, 8]
#[9, 10, 11, 12]
#[13, 14, 15, 16]
#Напишіть скрипт, який виведе цю матрицю на екран, обчислить та виведе суму елементів цієї матриці.
print("Here are some numbers, that's a matrix")
matrix_10 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
sum_matrix_10 = 0
for matrix_row in matrix_10:
    print(*matrix_row, sep = " ")
    sum_matrix_10 += sum(matrix_row)
print(f"Matrix sum is {sum_matrix_10}")

#Task 11
#Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
#Список може бути довільною довжиною.
import random
list_len_11 = random.randint(2, 20)
list_11 = [random.randint(0, 100) for num_11 in range(list_len_11)]
print("Random magic")
print(f"Random list of numbers incoming \n{list_11} \nAnd it was reversed \n{list_11[::-1]}")

#Task 12
#За допомогою циклів вивести на екран усі прості числа від 1 до 100.
import math
last_num_12 = int(input("I'll show you all prime numbers from 1 to *any* (define and input here): "))
list_12 = []
num_12 = 2
while num_12 <= last_num_12:
    if ((math.factorial(num_12 - 1) + 1) % num_12) == 0:
        list_12.append(num_12)
    num_12 += 1
print(f"It's {len(list_12)} prime numbers in this range")
print(f"All prime numbers from 1 to {last_num_12}:")
print(*list_12, sep = ", ")
#Answer 2, no list
import math
last_numm_12 = int(input("I'll show you all prime numbers from 1 to *any* (define and input here): "))
amount_12 = 0
numm_12 = 2
print(f"All prime numbers from 1 to {last_numm_12}:")
while numm_12 <= last_numm_12:
    if ((math.factorial(numm_12 - 1) + 1) % numm_12) == 0:
        amount_12 += 1
        print(numm_12, end = "  ")
    numm_12 += 1
print()
print(f"It's {amount_12} prime numbers in this range")

#Task 13
#Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури (число непарне).
width_13 = int(input("I want to draw a sandglass. Define it's width, please (the number must be Odd and bigger then 2): "))
if width_13 % 2 == 0 or width_13 < 3:
    print("Can you even read?! I'm depressed, I drow nothing. Bye")
else:
    print("Look at this beauty!")
    for num_13 in range(width_13, 0, -2):
        space = (width_13 - num_13) // 2
        print("     " + " " * space + "*" * num_13)
    for num_13_low in range(3, width_13+1, 2):
        space = (width_13 - num_13_low) // 2
        print("     " + " " * space + "*" * num_13_low)
        