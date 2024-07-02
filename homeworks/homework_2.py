print("Kid's calculator game by VesTheCoder (lol)")
#Task 1
#Написати скрипт, який виводить задане число на екран, лише якщо введене число від’ємне.
num_1 = int(input("Try to input the correct number that I will show you after your input > "))
num_1 < 0 and print(f"{num_1}, great job!") or num_1 > 0 and print("Wrong, better luck next time!")


#Task 2
#Написати скрипт, який перевіряє, чи введене користувачем цілочисельне значення менше 20 чи ні.
num_2 = int(input("give me a number to tell you if it's smaller ar greater then 20 > "))
num_2 < 20 and print("It is smaller then 20!") or num_2 > 20 and print("That's bigger then 20!") or num_2 == 20 and print("That's exactly 20!")


#Task 3
#Написати скрипт, який перевіряє, чи введене користувачем цілочисельне значення дорівнює нулю чи ні.
num_3 = int(input("Please input 0 (zero) or any other number > "))
num_3 == 0 and print("Hey, that's a zero, great!") or num_3 != 0 and print("Man, that's not a zero, come on")


#Task 4
#Написати скрипт, який перевіряє, чи введене користувачем цілочисельне значення є парним чи непарним.
num_4 = int(input("Give me any number to see if it's paired or unpaired > "))
num_4 % 2 == 0 and print("This one is paired!") or num_4 % 2 != 0 and print("This one is unpaired!")


#Task 5
#Написати скрипт, який повертає найбільше число серед трьох, які введені користувачем.
#Решение 1
num5 = int(input("Input some random number > "))
num6 = int(input("Input another random number > "))
num7 = int(input("Input the last random number > "))
print(f"The biggest one of those is {max(num5, num6, num7)}!")
#Решение 2
print(f"I repeat: the biggest one of those is {num5 >= num6 and num5 >= num7 and num5 or num6 >= num5 and num6 >= num7 and num6 or num7}!")


#Task 6
#Написати скрипт, який запитує користувача, чи він володіє посвідченням водія (yes або no). Якщо користувач відповідає "yes", виведи повідомлення "Ви можете керувати автомобілем". Якщо користувач відповідає "no", виведи повідомлення "Ви не можете керувати автомобілем".
question = input("Do you have a driver licence? Answer 'yes' or 'no' > ")
question == "yes" and print("You can drive the car!") or question == "no" and print("You can not drive the car!") or question != "no" and question != "yes" and print("you gave me the wrong answer u fool!")


#Task 7
#Написати скрипт, який запитує користувача про його вік і перевіряє, чи він відповідає критеріям для отримання прав на керування автомобілем. Критерії: користувач повинен бути старше 18 років.
#Якщо користувач задовольняє критерії, виведи повідомлення "Ви можете отримати посвідчення водія". Якщо користувач не задовольняє критерії, виведи повідомлення "Ви не відповідаєте критеріям для отримання посвідчення водія".
user_age = int(input("Input your age (as a number) > "))
user_age >= 18 and print("You grown enough to drive any vihecle you want!") or user_age < 18 and user_age >=16 and print("You can drive only a bike, no cars for you!") or user_age < 16 and print("You can't get a driver licence for now, sad times")



#Task 8
#Написати скрипт, який перевіряє, чи введене число є додатнім і парним. Виведи повідомлення "Число є додатнім і парним", якщо число задовольняє обидва критерії. В іншому випадку, якщо число не є додатнім або не є парним, виведи повідомлення "Число не задовольняє критерії".
#Наприклад, якщо користувач вводить число 6, програма повинна вивести "Число є додатнім і парним". А якщо користувач вводить число -3, програма повинна вивести "Число не задовольняє критерії".
num8 = int(input("Try to give me a number and see if it matches my cryterias > "))
num8 > 0 and num8 % 2 == 0 and print("That's a gues! The number is positive and paired!") or print("Ah, you didn't guesed the right criterea. Better luck next time")


#Task 9
#Написати скрипт, який перевіряє, чи введене число є кратним 3, але не є кратним 5. Якщо число задовольняє ці критерії, виведи повідомлення "Число підходить". В іншому випадку виведи повідомлення "Число не підходить".
num9 = int(input("Let's try again. Give me any number > "))
num9 % 3 == 0 and num9 % 5 != 0 and print("This one matches, great number!") or print("I fooled you and changed my matching criterea, this number doesn't feets neather.")

print("Thanks for your time and best regards, User!")