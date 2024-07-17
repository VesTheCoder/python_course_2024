# Task 1
# Напишіть скрипт, який порахує скільки літер «b» у введеному рядку тексту.
text_1 = input("Type your text and the amount of 'b' letters would be counted: ")
fold_1 = text_1.casefold()
search_1 = fold_1.count("b")
print(f"U used {search_1} letters 'b'. It's good those are unlimmited")

# Task 2
# Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного ім'я на валідність 
# (мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно починатися з великої літери, за якою повинні йти маленькі).
name_2 = input("Input your name correctly: ")
while not (name_2[0].isupper() and name_2[1:].islower() and name_2.isalpha()):
    print("That's not a correct spelling, please repeat your input.")
    name_2 = input("Input your name correctly: ")
else:
    print(f"That's right, your name is {name_2}, my pleasure to meet you!")


# Task 3
# Напишіть скрипт, який обчислює суму всіх кодів символів рядка.
#НЕ ПОНЯЛ ЗАДАНИЕ, НЕ ДОСТАТОЧНО ЗНАНИЙ
user_text_3 = input("Input any text and I'll count the sum weight of all characters in it: ")
sum_3 = sum(ord(character) for character in user_text_3)
print(f"the answer is {sum_3}. \nShiiiiiet, that's a lot!")

# Task 4
# Виведіть на екран 10 рядків із значенням числа Pi. У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.
# Задачу усложнил до варианта игры.
import math
pi_num = f"{math.pi:.12f}"
print("How many digits of Pi do you know? Let's test you!")
print(f"Pi starts with {pi_num[:4]}")
for p in range(4, 14):
    user_input_4 = input(f"What is the next digit? Input: ")
    if user_input_4 == pi_num[p]:
        print("That's right!")
    else:
        print("Wrong!")
    print(f"Pi is {pi_num[:p+1]} \nWe go on")
print("No, I'm lying, we're finished, that's enough.")


# Task 5
# Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.

# Task 6
# Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери). Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. 
# Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"

# Task 7
# Напишіть скрипт для очищення тексту від HTML-тегів.
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації. Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">