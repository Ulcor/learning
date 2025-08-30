def count_to_ten():
    num = 0
    while num < 11:
        print(num)
        num += 1

count_to_ten()


def count_to_one():
    num = 10
    while num > 0:
        print(num)
        num -= 1

count_to_one()


#
# Show values 2 from dict list
def show_groceries(grocery_list: list):
    stopper = len(grocery_list)
    while stopper > 0:
        # print(stopper)
        print(next(iter(grocery_list[-stopper].values())))
        stopper -= 1


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

show_groceries(grocery_list)

# print(grocery_list[0])