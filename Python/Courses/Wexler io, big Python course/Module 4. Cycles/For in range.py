# Range theory
print(list(range(10)))
print(list(range(3,9,3)))
print(len(list(range(3,9,3))))

# Output all values from range
for i in range(10):
    print(f"Printing {i}")

# len + range
grocery_list = [{'name': 'banana'}, {'name': 'apple'}]

print(len(grocery_list))

# Iterate by index of a value
for i in range(len(grocery_list)):
    print(f"Printing {grocery_list[i]['name']}")


# Enumerate. Add tuple with 1: value, 2: value...
print(list(enumerate(grocery_list)))

# Task 1
# Get queue size like 0+1+2+3
def get_queue_score(amount_of_people: int):
    total = 0
    for i in range(amount_of_people):
        total += i
    return total

print(get_queue_score(5))

# Task 2. Dicts in list


def evaluate_groceries(arr):
    for i in range(len(arr)):
        print(i + 1, arr[i]['name'])

input_dict = [{'name': 'Кофе', 'price': 200}]

evaluate_groceries(input_dict)
# print(input_dict['name'])

# The same but with enumerate
def evaluate_groceries(arr):
    for i, item in enumerate(arr):
        print(i + 1, item['name'])

input_dict = [{'name': 'Кофе', 'price': 200}]

evaluate_groceries(input_dict)

# Item in list checker # 1
def check_item_in_list(grocery_list: list, item: str):
    for i in grocery_list:
        if i['name'] == item:
            print(item)
            break  # eliminates duplicates somehow

# Item in list checker # 2
def check_item_in_list(grocery_list: list, item: str):
    for i in grocery_list:
        if i['name'] == item:
            print(item)
            return
        # Так как return прерывает выполнение функции
        # если нужный элемент найден, следующая строка не сработает
    print(f"Продукта {item} нет в списке")

groceries = [{'name': 'Мясо', 'price': 100}, {'name': 'Рыба', 'price': 80}]
check_item_in_list(groceries, "Мясо")  # распечатает Мясо
check_item_in_list(groceries, "Молоко")  # ничего не распечатает, потому что молока нет в списке

# Leap years
def leap_years(start: int, finish: int, period: int):
    for year in range(start, finish, period):
        print(year)


leap_years(start=2000, finish=2101, period=4)


# even and odd
def even_numbers(target):
    for num in range(target):
        if num % 2 == 0:
            print(num)


def odd_numbers(target):
    for num in range(target):
        if num % 2 == 1:
            print(num)