# Task 1
# Необхідно підготувати звіт про витрати членів родини на новорічні свята.
# Дані по витратам наведено у файлі hw_10_test.txt у форматі:
# Номер за переліком Прізвище та ім'я (або ім'я) Сума Категорія товару
# Звіт повинен включати наступне:
# 1. Яка загальна сума витрат по кожній категорії товарів?
# 2. Скільки грошей витратив кожен член родини?
# 3. Яку кількість покупок та на яку загальну суму зробив введений користувачем через input член родини?

def func_cut_data(string):
    '''
    Converts the data strings into dictionarable parts and returns those.
    '''
    parts = string.strip().split(' ')
    category = parts[-1]
    amount = float(parts[-2].strip('$'))
    name = ' '.join(parts[1:-2])
    return name, amount, category

def func_calculate(file):
    '''
    Reads th file, creates dictionaries by category and by person and returns those.
    '''
    by_category = {}
    by_person = {}
    with open(file, 'r', encoding='utf-8') as file:
        for string in file:
            name, amount, category = func_cut_data(string)
            if category not in by_category:
                by_category[category] = 0
            by_category[category] += amount
            if name not in by_person:
                by_person[name] = 0
            by_person[name] += amount
    return by_category, by_person

def func_person(file, person):
    '''
    Reads th file, counts categorized and total spend ($), and the amount of purchaces by person. Returns all three values.
    '''
    count = 0
    total_amount = 0
    by_category_solo = {}
    with open(file, 'r', encoding='utf-8') as file:
        for string in file:
            name, amount, category = func_cut_data(string)
            if name == person:
                count += 1
                total_amount += amount
                if category not in by_category_solo:
                    by_category_solo[category] = 0
                by_category_solo[category] += amount
    return count, total_amount, by_category_solo

def main():
    '''
    Interacts with the user.
    '''
    init = input('I have your file! Would you like to get the information categorized? (y/n) ').upper()
    if init == 'Y':
        file_dat = 'homeworks\hw_10_test.txt'
        by_category, by_person = func_calculate(file_dat)
        print(f'Great! \n\nTotal spend by category:')
        for category, total in by_category.items():
            print(f'{category.capitalize()}: ${total:.2f}')
        print('\nTotal spend by person:')
        for member, total in by_person.items():
            print(f'{member}: ${total:.2f}')
        while True:
            person = input('\nEnter the person name for their purchase details (or "Exit" if you finished): ').title().strip()
            if person == 'Exit':
                print(f'\nThank you and thank me! Bye!')
                break
            count, total_amount, by_category_solo = func_person(file_dat, person)
            print(f'\n{person} made {count} purchases and spent ${total_amount:.2f} in total.')
            print(f'\n{person} spent by category:')
            for category, amount in by_category_solo.items():
                print(f'{category.capitalize()}: ${amount:.2f}')
    else:
        print('Ok, just messing around? Get back when you fix your head!')

if __name__ == "__main__":
    main()