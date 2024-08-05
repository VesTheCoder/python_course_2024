# Task 1
# Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці. На одному поверсі - 4 квартири. 
# Напишіть програму, яка від користувача отримує номер квартири та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі. 
# Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.
apt_num = int(input("Good day, sir! If you want to get inside the closed territory of our complex, please input the number of the apartment you want to get in > "))
if apt_num < 1 or apt_num > 4 * 9 * 4:
    print("You don't belong here, GERARA HERE MAN")
else:
    apt_per_floor = 4
    apt_per_door = 9 * apt_per_floor
    
    door = (apt_num - 1) // apt_per_door + 1
    floor = (apt_num - 1) % apt_per_door // apt_per_floor + 1
    apartment_on_floor = (apt_num - 1) % apt_per_floor + 1
    
    print(f"Great! You need to get to \n Door # {door} \n Floor # {floor} \n Apartment # {apartment_on_floor} on the floor \nI'm watching you!")



# Task 2
# Написати програму, яка буде повертати для заданого року кількість днів. 
# Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400
year = int(input("Choose any year, I would tell you if is it leap or regular > "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It's a leap year, 366 days!")
else:
    print("It's a regular year, 365 days!")


# Task 3
# Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої. Дано: A, B, C - сторони трикутника. 
# Напишіть програму, яка вказує чи існує такий трикутник.
print("Input 3 numbers, that would be taken as lengths of the sides of the triangle > ")
side_a = float(input("Input the lenght of side A > "))
side_b = float(input("Input the lenght of side B > "))
side_c = float(input("Input the lenght of side C > "))
if side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b:
    print("Triangle can be drawn with these lengths!")
else:
    print("Triangle can not be drawn with these lengths!")


# Task 4
# Попросіть користувача ввести пароль. 
# Якщо введений пароль співпадає з певним заздалегідь заданим паролем, вивести "Доступ дозволено", інакше - "Доступ заборонено".
password = "admin"
user_pass = input("Try to guess my password, user! Input here > ")
if user_pass == password:
    print("Password is correct! Access granted")
else:
    print("Password is incorrect! Access denied")

# Task 5
# Попросіть користувача ввести суму покупки. Якщо сума перевищує 1000 гривень, застосуйте знижку у розмірі 10% і виведіть загальну суму до сплати.
spent_by_user = float(input("We have a special discount if you spend more then 1000 UAH! What's your spend amount? Input here > "))
if spent_by_user > 1000:
    discount = spent_by_user * 0.9
    print(f"Great, you are getting a 10% dicsount! The final purchase price would be {discount:.2f} UAH!")
else:
    print(f"Sorry, you didn't spent enough. No discount for you, please pay {spent_by_user:.2f} UAH.")

# Task 6
# Попросіть користувача ввести номер місяця (1-12). Виведіть кількість днів у цьому місяці. (Зверніть увагу на високосні роки для лютого.)
user_month = int(input("if you want to know the amount of days on any month, please input the month number (1-12) > "))
if user_month < 1 or user_month > 12:
    print("Sorry, the year has only 12 months, your number is bullshit!")
elif user_month in (4, 6, 9, 11):
    print("it's 30 days in this month.")
elif user_month == 2:
    what_year = int(input("Amount of days in February depends on the year. What is the year? > "))
    if what_year % 4 == 0 and what_year % 100 != 0 or what_year % 400 == 0:
        print("It's 29 days in this month.")
    else:
        print("it's 28 days in this month.")
else:
    print("it's 31 days in this month.")



# Task 7
# Попросіть користувача ввести рейтинг обслуговування (від 1 до 5). 
# Виведіть відповідне повідомлення про рівень обслуговування (наприклад, "Відмінно", "Добре", "Задовільно", "Погано", "Жахливо").
# Answer 1
rating = float(input("Please rate or servise from 1 (awful) to 5 (excelent) > "))
if rating < 1:
    print("Sorry, it must be a mistake, have a good day!")
elif rating > 5:
    print("Wow, thanks, I'd take is as a double 'Excelent'! Have a good day!")
elif rating >= 4.5:
    print("I record it as 'Excelent'! Have a good day!")
elif rating >= 3.5:
    print("I record it as 'Good'! Have a good day!")
elif rating >= 2.5:
    print("I record it as 'OK'! Have a good day!")
elif rating >= 1.5:
    print("I record it as 'Bad'! Sorry and have a good day!")
else:
    print("I record it as 'Awful'! Sorry and have a good day!")

#Answer 2
rating2 = int(input("Please rate my servise from 1 (awful) to 5 (excelent) > "))
if rating2 == 5:
    print("I record it as 'Excelent'! Have a good day!")
elif rating2 == 4:
    print("I record it as 'Good'! Have a good day!")
elif rating2 == 3:
    print("I record it as 'OK'! Have a good day!")
elif rating2 == 2:
    print("I record it as 'Bad'! Sorry and have a good day!")
elif rating2 == 1:
    print("I record it as 'Awful'! Sorry and have a good day!")
else:
    print("Answer is incorrect. Learn to read first, silly.")

# Task 8
# Попросіть користувача ввести свою вагу (в кілограмах) та зріст (в метрах).
# Обчисліть і виведіть індекс маси тіла (BMI) за формулою: BMI = вага / (зріст^2). 
# Далі виведіть відповідне повідомлення про стан ваги (наприклад, "Недостатньо ваги", "Нормальна вага", "Надлишкова вага", "Ожиріння").
print("Let's see what is your body condition")
user_weight = float(input("Please tell me your weight in kilograms > "))
user_heith = float(input("Please tell me your height in meters > "))
count_index = user_weight / (user_heith**2)
if count_index >= 30:
    print("You're fat! Go lose some kilos NOW!")
elif count_index >= 25:
    print("You're a little fat. Eat less pizza.")
elif count_index >= 18.5:
    print("Your weight is ok, well done!")
elif count_index >= 16:
    print("You're a little thin, but that's fine.")
else:
    print("You weight nothing! Be avare of strong winds and eat more!")
