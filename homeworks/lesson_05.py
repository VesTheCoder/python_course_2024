# Task 1
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun")
sal_list = []
sal_list.append(float(input("Your compensation for month 1 ($): ")))
sal_list.append(float(input("Your compensation for month 2 ($): ")))
sal_list.append(float(input("Your compensation for month 3 ($): ")))
sal_list.append(float(input("Your compensation for month 4 ($): ")))
sal_list.append(float(input("Your compensation for month 5 ($): ")))
sal_list.append(float(input("Your compensation for month 6 ($): ")))
avg_sal = sum(sal_list) / len(sal_list)
min_sal = min(sal_list)
max_sal = max(sal_list)
min_index = sal_list.index(min(sal_list))
max_index = sal_list.index(max(sal_list))

print(f"Your max compensation was ${max_sal:.2f} \nYour min compensation was ${min_sal:.2f} \nYour avarage compensation was ${avg_sal:.2f}.")
print(f"Max earnings month was {months[max_index]}. \nMix earnings month was {months[min_index]}. \nGreat job!")


# Task 2
months = ("Jan", "Fab", "Mar", "Apr", "May", "Jun")
sal_list = []
while len(sal_list) < 6:
    sal = float(input("Input your monthly compensation, up to 6 times: "))
    if sal > 0:
        sal_list.append(sal)
    else:
        print("Compensation can not be less the 0, variable wasn't added to the list")

avg_sal = sum(sal_list) / len(sal_list)
min_sal = min(sal_list)
max_sal = max(sal_list)
min_index = sal_list.index(min(sal_list))
max_index = sal_list.index(max(sal_list))

print(f"Your max compensation was ${max_sal:.2f} \nYour min compensation was ${min_sal:.2f} \nYour avarage compensation was ${avg_sal:.2f}.")
print(f"Max earnings month was {months[max_index]}. \nMix earnings month was {months[min_index]}. \nGreat job!")
