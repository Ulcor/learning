def divide_numbers(first, next):
    return first / next


# first = 2
# next = 1  # if 0, raise exception
# print(divide_numbers(first, next))

def safe_division(first, next):
    try:
        return divide_numbers(first, next)
    except ZeroDivisionError as error:
        return 0


first = 10
next = 2  # if 0, raise exception
print(safe_division(first, next))