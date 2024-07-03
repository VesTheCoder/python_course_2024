#Task 1
day_num = int(input("Введите какой-то день недели числом (от 1 до 7) > "))
if day_num == 1:
    print("it's Mon!")
elif day_num == 2:
    print("it's Tue!")
elif day_num == 3:
    print("it's Wed!")
elif day_num == 4:
    print("it's Thu!")
elif day_num == 5:
    print("it's Fri!")
elif day_num == 6:
    print("it's Sat!")
elif day_num == 7:
    print("it's Sun!")
else:
    print("Number doesn't match")

#Task 2
grade = int(input("how many points did you got for the test (input from 0 to 100)? > "))
if grade < 0 or grade > 100:
    print("that's a wrong number!")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
elif grade >= 50:
    print("E")
else:
    print("F")

