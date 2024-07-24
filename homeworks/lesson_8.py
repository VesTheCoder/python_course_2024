#Task 1
data = [
    '1 Bob Simson 19.58$ decorations',
    '2 Mary 66.7$ food',
    '3 Mary 98.91$ toys',
    '4 Aleksa 72.29$ drinks',
    '5 Maria Simson 84.48$ food',
    '6 Aleksa 100.41$ accessories',
    '7 Mary 19.9$ accessories',
    '8 Bob Simson 83.88$ drinks',
    '9 Bob Simson 58.21$ instruments',
    '10 Maria Simson 20.61$ accessories',
]
by_category = {}
for string in data:
    string_split = string.split()
    amount = float(string_split[-2].strip('$'))
    category = string_split[-1]
    if category in by_category:
        by_category[category] += amount
    else:
        by_category[category] = amount
print("Spent by categories:")
for item, total in by_category.items():
    print(f"{item}: {total:.2f}$")

#Task 2
text1 = input("Input your text: ").split()
text2 = input("Input another text: ").split()
print(f"You repeated the word(s) {set(text1) & set(text2)}")