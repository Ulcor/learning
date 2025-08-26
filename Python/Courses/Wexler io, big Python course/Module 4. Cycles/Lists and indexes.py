list_1 = list(range(10))
# ctrl + click to see builtins.py, and all methods in it
list_1.remove(1)
list_1.append(2)
list_1.index(0)

print(list_1)

list_1 = list_1.pop(2)

print(list_1)

# Write add_to_grocery_list function
to_buy = ['avocado', 'milk', 'eggs']

def add_to_grocery_list(grocery_list: list, new_item: str):
    grocery_list.append(new_item)


def remove_last_from_grocery_list(grocery_list: list):
    return grocery_list.pop()

remove_last_from_grocery_list(to_buy)

def remove_first_from_grocery_list(grocery_list: list):
    return grocery_list.pop(0)

remove_first_from_grocery_list(to_buy)

# Delete by index
def remove_from_grocery_list(grocery_list: list, remove: str):
    try:
        grocery_list.pop(grocery_list.index(remove))
    except ValueError as error:
        print(error)

removed = remove_from_grocery_list(to_buy, 'milk')   # milk
remove_from_grocery_list(to_buy, 'chicken')  # вызовет ошибку ValueError

print(removed)
print(to_buy)

to_buy = ['avocado', 'milk', 'eggs']

# Delete by index but simpler
def remove_from_grocery_list(grocery_list: list, item: str):
    return grocery_list.pop(grocery_list.index(item))

removed = remove_from_grocery_list(to_buy, 'milk')   # milk
# remove_from_grocery_list(to_buy, 'chicken')  # вызовет ошибку ValueError

print(removed)
print(to_buy)

# List v2
workers = ['John', 'Doe', 'Michael', 'Mia', 'Lara']

def get_first(names: list):
    return names[0]

print(get_first(workers))

def get_last(names: list):
    return names[-1]

print(get_last(workers))

# Inversion
def get_workers(names: list):
    return names[::-1]

print(get_workers(workers))

# First 2 indexes
def get_champions(names: list):
    return names[0:2]

print(get_champions(workers))

# Last 3 indexes
def get_slobs(names: list):
    return names[-3::]

print(get_slobs(workers))