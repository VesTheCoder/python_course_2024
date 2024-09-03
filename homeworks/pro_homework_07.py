# Task 1
# Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, 
# закон якої задається за допомогою функції користувача. 
# Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, 
# що видаються послідовностю. Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
stop_here = int(input("SOME RANDOM NUMBER OVER HERE NOW: "))
def custom_sequence(start: int, count: int, user_function: callable): #Правильно ли писать тут callable???
    current_count = 0
    while current_count < count:
        yield user_function(start)
        current_count += 1
        start += 1

for i in custom_sequence(1, stop_here, lambda a: stop_here // a):
    print(i)


# Task 2
# Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація - https://en.wikipedia.org/wiki/Memoization .
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі. 
# Порівняйте швидкість виконання із просто рекурсивним підходом.
def fibo():
    buffer = {}
    def fibo_count(num):
        if num < 2:
            return num
        if num in buffer:
            return buffer[num]
        buffer[num] = fibo_count(num - 1) + fibo_count(num - 2)
        return buffer[num]
    return fibo_count

fibo = fibo()
for i in range(20000):
    print(fibo(i))



# Task 3
# Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.
test_list = [1,2,2]

def test_func(num):
    return num*-num

print(list(map(test_func, test_list)))
