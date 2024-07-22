# Task 1
# Напишіть скрипт, який порахує скільки літер «b» у введеному рядку тексту.
text_1 = input("Type your text and the amount of 'b' letters would be counted: ")
search_1 = text_1.casefold().count("b")
print(f"You used {search_1} letters 'b'. It's good those are unlimmited")

# Task 2
# Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного ім'я на валідність 
# Задачу усложнил до цикла ввода пока имя не будет правильным.
name_2 = input("Input your name correctly: ")
while not name_2.istitle() and name_2.replace(" ", "").isalpha():
    print("That's not a correct spelling (don't forget to start with a capital letter), please repeat your input.")
    name_2 = input("Input your name correctly: ")
else:
    print(f"Now that's a valid name, my pleasure to meet you!")


# Task 3
# Напишіть скрипт, який обчислює суму всіх кодів символів рядка.
user_text_3 = input("Input any text and I'll count the sum weight of all characters in it: ")
sum_3 = sum(ord(character) for character in user_text_3)
print(f"The answer is {sum_3}. \nShiiiiiet, that's a lot!")

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
# Добавил цикл замены пунктуационных знаков на всякий случай
import string
user_input_5 = input("Type in any text, I'll find the longest word: ").lower()
for item in string.punctuation:
    user_input_5 = user_input_5.replace(item, "")
split_5 = user_input_5.split()
max_word = split_5[0]
for item in split_5:
    if len(item) > len(max_word):
        max_word = item
print(f"The longest word is '{max_word}'.")

# Task 6
# Вовочка писав поспіль однакові слова (слово може складатися з однієї літери). Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. 
# Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад: catcatcatcat - Вовочка писав слово - "cat"
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
# Нагуглил документацию по регулярным выражениям и разобрался в люгике синтаксиса.
import re
user_input_7 = input("Give me any text with HTML tags to remove all HTML tags: ")
print(f"The text is: {re.sub(r"\<[^>]*\>","", user_input_7)}")

# Task 7 РЕШЕНИЕ 2
user_input_8 = input("Give me any text with HTML tags to remove all HTML tags: ")
while "<" in user_input_8 and ">" in user_input_8:
    tags_open = user_input_8.find("<")
    tags_close = user_input_8.find(">")   
    user_input_8 = user_input_8[:tags_open] + user_input_8[tags_close + 1:]
print(f"The text is: {user_input_8}")