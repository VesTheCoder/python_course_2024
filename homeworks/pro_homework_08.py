# Task 1
# Напишіть декоратор, який виконує певну дію перед і після виконанням функції.
def double_trouble(func):
    def wrapper(*args, **kwargs):
        print(f"Imagine we did something first, then we exewcute the function '{func.__name__}'")
        print(func(*args, **kwargs))
        print("And here we did something again, after the function execution")
        return f"And we're done"
    return wrapper

@double_trouble
def some(arg):
    return f"{arg}"

print(some("ha-ha-ha"))

# Task 2
# Напишіть декоратор, який зберігає результати обчислення функції у файл для подальшого використання.
def result_saver(func):
    def wraper(*args, **kwargs):
        with open("result_file.txt", "a") as file:
            file.write(f"{func(*args, **kwargs)}\n")
    return wraper

@result_saver
def multiplier(a, b):
    return a * b

multiplier(6, 9)
multiplier(4, 20)

# Task 3
# Напишіть декоратор, який перехоплює та обробляє виключення, що виникають у функції.
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as lol:
            return f"Gratz, you made a mistake and got the error: {lol}"
    return wrapper

@exception_decorator
def multiplier(a, b):
    return a / b

print(multiplier(69, 0))

# Task 4
# Напишіть декоратор, який вимірює час виконання функції.
import datetime
import math
import sys
sys.set_int_max_str_digits(1000000)

def execution_timer(func):
    def wraper(*args, **kwargs):
        start = datetime.datetime.now()
        execution = func(*args, **kwargs)
        end = datetime.datetime.now()
        return f"{execution}.\nIt took {end - start} secs to execute the function."
    return wraper

@execution_timer
def factorial_to_file(num):
    with open("big_number.txt", "a") as file:
        file.write(f"#Start\n{math.factorial(num)}\n#End\n")
    return f"We're done"

print(factorial_to_file(69_420))

# Task 5
# Напишіть декоратор, який логує аргументи та результати функції.
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def log_decorator(func):
    def wrapper(*args, **kwargs):
        if kwargs:
            logging.info(f"Function '{func.__name__}' called with args: {args}, kwargs: {kwargs}")
        else:
            logging.info(f"Function '{func.__name__}' called with args: {args}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned the result: {result}")
        return result
    return wrapper

@log_decorator
def test_func(a, b, c, d):
    return a + b + c + d

print(test_func(69, 69, 69, 69))

# Task 6
# Напишіть декоратор, який обмежує кількість викликів функції.
# Решение 1 - простое.
def call_limiter(func):
    calls_amount = 0
    def wrapper(*args, **kwargs):
        nonlocal calls_amount
        if calls_amount < 2:
            calls_amount += 1
            return func(*args, **kwargs)          
        else:
            raise Exception(f"Max {calls_amount} calls of '{func.__name__}' function, sorry!")
    return wrapper
# Решение 2 - ограничиваем кол-во вызовов каждой функции отдельно.
def call_limiter(func):
    calls_amount = {}
    def wrapper(*args, **kwargs):
        if func.__name__ in calls_amount:
            calls_amount[func.__name__] += 1
        else: 
            calls_amount[func.__name__] = 1
        if calls_amount[func.__name__] < 3:
            return func(*args, **kwargs)
        else:
            return f"Max {calls_amount[func.__name__] - 1} calls of '{func.__name__}' function, sorry!"
    return wrapper

@call_limiter
def some_func(arg):
    return f"Hi, {arg}, my dude!"

@call_limiter
def some_func2(arg):
    return f"Double-Hi, {arg}, my dude!"

print(some_func("Oleg"))
print(some_func("Oleh"))
print(some_func("Vlad"))
print(some_func2("Oleg"))
print(some_func2("Oleh"))
print(some_func2("Vlad"))


# Task 7
# Напишіть декоратор, який кешує результати обчислення функції і повертає їх з кешу при наступних викликах з тими самими аргументами.
def cache_results(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache: 
            return cache[key]
        else:
            cache[key] = func(*args, **kwargs)
            return func(*args, **kwargs)
    return wrapper

@cache_results
def triple_multiplier(n):
    return n * 3

print(triple_multiplier(210))
print(triple_multiplier(210))