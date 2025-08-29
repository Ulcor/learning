# Натуральный цикл / Natural cycle
def show_groceries_simple(grocery_list: list):
    for item in grocery_list:
        print(item)

g_list = ['bread', 'milk', 'beans']

show_groceries_simple(g_list)

# Show values from dict list
grocery_list = [
    {'name': 'Сметана',
     'price': 50},
    {'name': 'Кофе',
     'price': 150},
    {'name': 'Торт',
     'price': 500},
    {'name': 'Пиво',
     'price': 90},
]

def show_groceries(grocery_list: list):
    for pair in grocery_list:
        print(pair['name'])

    # V1
    # for pair in grocery_list:
    #     key = pair.values()
    #     iterator = iter(key)
    #     print(next(iterator))



show_groceries(grocery_list)

# Show values 2 from dict list
def get_sum(grocery_list):
    for pair in grocery_list:
        print(pair['price'])

get_sum(grocery_list)

# Show sum of values 2 from dict list
def get_sum(grocery_list: list, price_increase: int):
    total = 0
    for pair in grocery_list:
        total += pair['price'] + price_increase
    return total

print(get_sum(grocery_list=grocery_list, price_increase=5))

# Price X - Price Y
def get_addition(grocery_list: list):
    total = 0
    total_1 = 0
    for pair in grocery_list:
        total += pair['price']
    for pair in grocery_list:
        total_1 += pair['price'] * 1.15
    return total_1 - total

get_addition(grocery_list)