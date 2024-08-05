#Task 1:
#Привітання користувача. Напишіть Python-скрипт, який вітає користувача за його ім'ям.
#Ім'я вводить користувач з клавіатури за допомогою функції input, а потім виводиться привітання за допомогою функції print.
username=input("Hey, I'm a stupid python program, my name is Jarvis! What's your name? Type it here: ")
print(f"Hey, {username}! Nice to meet you! (not)")


#Task 2:
#Написати Python-скрипт, який для п'яти цілочисельних значень (вводить користувач з клавіатури), знаходить мінімум, максимум та середнє.
#Для пошуку мінімального та максимального значення потрібно використовувати функції min, max.
print("Now, let's play the game. Please input 5 random numbers and I'll show you the smallest, the biggest, and the avarage of those numbers! Start your input here")
n1 = int(input("Your first number is: "))
n2 = int(input("Your second number is: "))
n3 = int(input("Your third number is: "))
n4 = int(input("Your fourth number is: "))
n5 = int(input("Your last number is: "))
numbers = [n1, n2, n3, n4, n5]
minimum = min(numbers)
maximum = max(numbers)
average = sum(numbers)/5
print(f"Your smallest number is {minimum}, your biggest number is {maximum} and the avarage of all five is {average}. I'M SMART YOU SEE, {username}?!")


#Task 3:
#Написати Python-скрипт, який буде повертати результат арифметичних дій +, -, *, /, // для заданих x та y (вводить користувач з клавіатури)
print("Now I'm a calculator. Gimmie 2 more numbers and I'll show you more math. Start your input here")
x=float(input("Input any number here - it would be your first number >"))
y=float(input("Input any number here - it would be your second number >"))
your_sum=x+y
deductionx=x-y
deductiony=y-x
mult=x*y
devidex=x/y
devidey=y/x
dudex=x//y
dudey=y//x
print(f"Get ready {username}, this would blow your mind!\n x+y={your_sum}\n x-y={deductionx}\n y-x={deductiony}\n x*y={mult}\n x/y={devidex}\n y/x={devidey}\n x//y={dudex}\n y//x={dudey}\nISN'T THAT MAGICK????")


#Task 4:
#Написати Python-скрипт, який для кола заданого радіуса (вводить користувач з клавіатури) знаходить діаметр, довжину і площу окружності.
import math
print(f"R u ready for some GEOMETRY, {username}? Let me do some circle magic!")
radius=float(input("Pick any number, I would take it as a radius of a circle >"))
diameter=2*radius
circlelength=math.pi*2*radius
area=radius**2*math.pi
print(f"OK, so the radius is {radius}.\nThe diameter would be {diameter}\nOkruznost would be {circlelength}\nAnd the area of the circle would be {area}.\nThat's too easy")


#Task 5:
#Деякі інвестиційні консультанти вважають, що розумно очікувати 5% *годовых после инфляции* прибутку в довгостроковій перспективі на фондовому ринку *США*.
#Припускаючи, що ви починаєте з 1000 доларів і *реинвестируете прибыль каждый год*, обчисліть і відобразіть, скільки грошей ви матимете через 10, 20 і 30 років.
print(f"Now, {username}, I think we're close enought for money operations. I demand you to trust me your funds, I will invest those and we'll become rich. Let me show you how much money you would get in 10, 20 and 30 years.")
p_invest_amount=float(input("How much $$$ would you like to invest? Gimmie the amount >"))
r_year_yeald=0.05
a_10years=p_invest_amount*(1+r_year_yeald)**10
a_20years=p_invest_amount*(1+r_year_yeald)**20
a_30years=p_invest_amount*(1+r_year_yeald)**30
print(f"So, you would have\n ${a_10years} in 10 years!\n ${a_20years} in 20 years!\n ${a_30years} in only 30 years!\nGreat, right? SEND MONEY NOW")


#Task 6:
#Створіть скрипт-конвертер валюти, який запитує у користувача суму в доларах і переводить її в гривні згідно поточного обмінного курсу. Обмінний курс можна вказати в програмі.
print(f"Fine, {username}, jokes asside! I am a ukrainian bot, I have ukrainian interpreneurship. To receive the money from you, I need you to send the amount in HRYVNAS. Let me show you how much money I would expect from you in hryvnas")
ex_rate=40.46
ex_rate_amort=ex_rate/100*101
amount_to_send=float(input("Right here right now input the amount in $$$ you gonna send me (I hope it's at least a thousand bucks)"))
amount_uah=amount_to_send*ex_rate
amount_uah_amort=amount_to_send*ex_rate_amort
print(f"The amount in HRYVNAS would be {amount_uah} UAH\n BUT\nI would have to also count additional amortisation because of bank commisions.\n Send me {amount_uah_amort}UAH. Waiting 20 mins or else...")
sent=input("Type 'YES' when you'll send. You have no other option, dont even try ")

#Task 7:
#Написати скрипт, яких тризначне ціле число (вводить користувач з клавіатури) розділяє на окремі цифри. Кожну цифру треба вивести в окремому рядку.
#*ANSWER 1*
print(f"Money received.\nLet's play the last game, r u ready? A short one")
user_number_text=input("Input any 3-digits number from 100 to 999. Here >")
print(f"let me split it string by string\n {user_number_text[0]}\n {user_number_text[1]}\n {user_number_text[2]}")
#*ANSWER 2*
user_number=int(user_number_text)
edenitsi=user_number%10
desiatki=(user_number//10)%10
sotni=user_number//100
print(f"LOL, there's no point to do that, don't you think, {username}? Ok, let's try again! Here are your digits:\n {sotni}\n {desiatki}\n {edenitsi}\nHM, STILL KINDA NOTHING, just spending your time")
respect=input("I have your money now anyway. Press F to pay respect >")
print("Bye")
