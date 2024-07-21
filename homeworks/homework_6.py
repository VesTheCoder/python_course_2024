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
import string
user_input_5 = input("Type in any text, I'll find the longest word: ").lower()
for item in string.punctuation:
    user_input_5 = user_input_5.replace(item, ' ')
split_5 = user_input_5.split()
max_word = split_5[0]
for item in split_5:
    if len(item) > len(max_word):
        max_word = item
print(f"The longest word is '{max_word}'.")

# Task 6
# Вовочка писав поспіль однакові слова (слово може складатися з однієї літери). Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. 
# Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# catcatcatcat - Вовочка писав слово - "cat"
import string
user_input_6 = input("Type the word or a letter several times without the space, Vovochka: ").lower()
for item in string.punctuation:
    user_input_6 = user_input_6.replace(item, "")
length_6 = len(user_input_6)
for item in range(1, length_6 + 1):
    if length_6 % item == 0 and user_input_6[:item] * (length_6 // item) == user_input_6:
        word_6 = user_input_6[:item]
        break
print(f"The word is {word_6}. Don't worry, Vovochka!")

# Task 7
# Напишіть скрипт для очищення тексту від HTML-тегів.
import re
user_input_7 = input("Give me any text with HTML tags to remove all HTML tags: ")
print(f"The text is: {re.sub(r"\<[^>]*\>","", user_input_7)}")