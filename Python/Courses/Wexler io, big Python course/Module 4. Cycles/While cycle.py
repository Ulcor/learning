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

# Wait some time than stop
import time

def count_second():
    time_count = 0
    while time_count < 5:
        print(time_count)
        time_count += 1
        time.sleep(0.1)

count_second()

# Sleep timer
import time
def time_to_wake_up(sleep_time: int):
    if sleep_time > 8:
        return True # Пора вставать
    return False


def check_sleep(hours: int):
    while hours <= 24:
        return time_to_wake_up(hours), hours
        # time.sleep(0.1)  # (60*60)  # 1 hour
        # hours += 1
    return False, hours


print(check_sleep(hours=1)) # (False, 1)
print(check_sleep(hours=9))