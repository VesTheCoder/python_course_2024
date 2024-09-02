# Task 2
# Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.
#Решение 1
def progression_generator(start, stop, multiplyer):
    while start < stop+1:
        yield start
        start *= multiplyer
#Решение 2
def another_progression_generator(start, amount, multiplyer):
    for _ in range(amount):
        yield start
        start *= multiplyer

# Task 3
# Реалізуйте свій аналог генераторної функції range().
def custom_range(*args):
    if len(args) < 1 or len(args) > 3:
        raise TypeError("Invalid number of arguments, must be one, two or three")
    
    start, stop, step = 0, 10, 1
    if len(args) == 1:
        stop = args[0]
    if len(args) == 2:
        start = args[0]
        stop = args[1]
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    
    if step == 0:
        raise ValueError("sorry, step can't be 0, you're waisting the computing power!")
    if step > 0:
        if start > stop:
            raise ValueError("yo, stop can't be less than start, cause your step is positive!")
        while start < stop:
            yield start
            start += step
    else:
        if start < stop:
            raise ValueError("yo, start can't be less than stop, cause your step is negative!")
        while start > stop:
            yield start
            start += step

print(tuple(custom_range(1.5, 200, 2)))

# Task 4
# Напишіть генераторну функцію, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана параметром цієї функції.
def prime_generator(stop):
    for i in range(2, stop):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

result = tuple(prime_generator(69))
print(f"There are {len(result)} prime numbers in your range. \n{result}")

# Task 5
# Реалізуйте генераторну функцію для генерації послідовності дат. Початкова та кінцеві дати мають бути задані параметрами цієї функції.
import datetime
def date_generator(start_date, end_date):
    today = start_date
    while today <= end_date:
        yield today
        today += datetime.timedelta(days=1)