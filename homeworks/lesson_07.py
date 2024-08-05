#Есть список с данными. Сколько денег было потрачено на категорию еда(food)?
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
    '10 Maria Simson 20.61$ accessories'
]
food_cost = 0
for string in data:
    if 'food' in string:
            string_split = string.split()           
            amount = float(string_split[-2].replace("$", ""))
            food_cost += amount
print(f"DA FUCK! WE SPENT ${food_cost} ON FOOD! EAT LESS!!!")
