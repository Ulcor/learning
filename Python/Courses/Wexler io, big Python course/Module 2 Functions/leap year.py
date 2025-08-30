# / - деление
# // - деление без остатка

def is_leap_year(year):
    if year / 4 == year // 4:  #
        return True
    else:
        return False


print(is_leap_year(2023))