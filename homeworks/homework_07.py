# Task 1
# Напишіть програму, яка приймає рядок тексту і повертає словник, де ключами є слова, а значеннями - кількість входжень кожного слова в тексті.
# Усложнил задачу до возможности вводить пока юзер хочет.
dic_1 = {}
user_text_1 = input("Input your text and I'll count different words: (or type 'finish' to stop): ").lower()
while user_text_1 != "finish":
    user_text_1 = user_text_1.split()
    for item in user_text_1:
        dic_1[item] = dic_1.get(item, 0) + 1
    print("Counted for you:")
    print(*dic_1.items(), sep="; ")
    user_text_1 = input("Any other words? (or type 'finish' to stop): ")
else:
    print("Ok, chill, it's over")

# Task 2
# Реалізуйте простий перекладач, який використовує словник для збереження пар слів. Користувач може вводити слово, а програма повертає його переклад. 
# Дополнительно реализовал цикл взаимодействия с пользователем, чтоб он мог добавлять перевод сам и спрашивать этот перевод потом.
dic_2 = {
    "hello": "привіт",
    "goodbye": "до побачення",
    "cat": "кіт",
    "dog": "собака"
}
while True:
    word_2 = input("Input the word to translate to ukrainian or 0 (zero) to exit (only one word at a time): ").strip().lower()
    if word_2 == '0':
        print("Thanks, have a good day")
        break
    if dic_2.get(word_2):
        print(f"The translation of '{word_2}' is {dic_2.get(word_2)}")
    else:
        dic_2[word_2] = input(f"The translation of '{word_2}' isn't there. Input the translation manually to add it to the dictionary: ").strip().lower()
        print(f"The word '{word_2}' was added.")

# Task 3
# Реалізуйте просту програму для збереження контактів. Кожен контакт може мати ім'я як ключ та номер телефону як значення. 
# Дозвольте користувачу додавати нові контакти, видаляти існуючі та отримувати номер телефону за ім'ям.
dic_3 = {
    "emergency": "911",
    "jamesbond": "007",
}
print("This is your contact book. What do you want to do?")
while True:
    print()
    print("1 - Add new contact")
    print("2 - Delete contact")
    print("3 - Get the number of a contact by name")
    print("4 - End interaction")
    user_choice = input("Input the number of your choice (1, 2, 3 or 4): ")
    if user_choice not in ("1", "2", "3", "4"):
        print("Incorrect input. Please, try again.")
    elif user_choice == "1":
        name = input("The name of your new contact: ")
        name_corrected = name.strip().lower().replace(" ", "")
        phone = input("The phone number (digits only): ").strip()
        dic_3[name_corrected] = phone
        print(f"Added {name} to the contact book.")
    elif user_choice == "2":
        name = input("Input the name of the contact to delete: ")
        name_corrected = name.strip().lower().replace(" ", "")
        if name_corrected in dic_3:
            del dic_3[name_corrected]
            print(f"{name} deleted from the contact book.")
        else:
            print(f"{name} not found, try again.")
    elif user_choice == "3":
        name = input("Input the desired contact name to get the phone number: ")
        name_corrected = name.strip().lower().replace(" ", "")
        res = f"{name}'s phone number is: {dic_3[name_corrected]}" if name_corrected in dic_3 else f"{name} not found, try again."
        print(res)
    else:
        print("My pleasure to serve you, dumb fuck! Would happy to see you again.")
        break

# Task 4
# Напишіть програму, яка конвертуватиме суму з однієї валюти в іншу, використовуючи словник з курсами обміну.
dic_4 = {
    'usd': 1,
    'eur': 0.92,
    'gbp': 0.77,
    'uah': 25.1, #ПОМЕЧТАЕМ
}
print("This is currency converter.")
while True:
    print()
    print("Choose what to do:")
    print("1 - I want to get the conversion rate")
    print("2 - I want to exit the program")
    user_choice = input("Input the number of your choice (1 or 2): ")
    if user_choice == '2':
        print("Goodbye, human! Have a good life!")
        break
    if user_choice == '1':
        user_curr_1 = input("What currency do you have? (ex. USD): ").strip().lower()
        user_amount = float(input("OK! What's the amount? Input here: "))
        user_curr_2 = input("What currency do you want to get? (ex. UAH): ").strip().lower()
        if user_curr_1 in dic_4 and user_curr_2 in dic_4:
            convert = user_amount / dic_4[user_curr_1] * dic_4[user_curr_2]
            print(f"For {user_amount:.2f} {user_curr_1} you will get {convert:.2f} {user_curr_2}")
        else:
            print("Sorry, we don't have an exchange rate info for those currencies. Anything else?")   
    else:
        print("Incorrect input. Please, try again.")
