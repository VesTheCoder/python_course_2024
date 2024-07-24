# Task 1
# Напишіть програму, яка перевіряє, чи всі елементи в списку є унікальними.
import random
list_1 = [random.randint(0, 100) for i in range(15)]
print(f"Here's the list {list_1}")
if len(list_1) == len(set(list_1)):
    print("All elements of the list are unique")
else:
    print("There are repeated elements in the list")

# Task 2
# Напишіть програму, яка приймає список елементів і повертає кількість унікальних елементів.
import random
list_2 = [random.randint(0, 20) for i in range(15)]
print(f"Here's the list {list_2} \nThere are {len(set(list_2))} unique elements in this list")
print(f"To be exact, those are: {set(list_2)}")

# Task 3
# Напишіть програму, яка приймає словник і перевіряє, чи містяться в ньому унікальні значення.
dic_3 = {
    "hi" : "привіт",
    "bye" : "до побачення",
    "adeus" : "до побачення",
    "cat" : "кіт",
    "dog" : "собака"
}
dic_3_list = []
for i in dic_3:
    dic_3_list.append(dic_3[i])
res = "Dictionary values are unique" if len(dic_3_list) == len(set(dic_3_list)) else "Dictionary values aren't unique"
print(res)

# Task 4
# Припустимо, що у тебе є дані про дружбу між користувачами соціальної мережі:
# Напишіть програму для розрахунку спільних друзів у соціальній мережі, імена яких задає користувач.
dic_4 = {
    "Alex": {"Paul", "David", "John"},
    "Paul": {"Alex", "David"},
    "David": {"Alex", "Paul", "John"},
    "John": {"Alex", "David"}
}
print("I'm an FBI agent and would now tell you who knows who")
firstuser_4 = input("Tell me the name of your friend: ").strip().casefold().capitalize()
seconduser_4 = input("Tell me the name of another friend: ").strip().casefold().capitalize()
if firstuser_4 not in dic_4 and seconduser_4 not in dic_4:
    print("I don't know the connections of those people, they are low profile")
else:
    in_common_4 = dic_4[firstuser_4].intersection(dic_4[seconduser_4])
print(f"{firstuser_4} and {seconduser_4} both know", end=" ")
print(*in_common_4, sep=' and ')

# Task 5
# Напишіть програму, яка повертає найдовше слово, яке міститься одночасно у двох рядках.
print("Now I'll show you the longest common word from your two sentences")
first_user_input_5 = input("Enter the first sentence: ").strip().casefold().split()
second_user_input_5 = input("Enter the second sentence: ").strip().casefold().split()
compare_5 = set(first_user_input_5).intersection(second_user_input_5)
print(f"The longest common word is {max(compare_5, key=len)}")