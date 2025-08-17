age = "35sds"  # will raise an error
# age = 35

try:
    age = int(age)
    print(age + 1)
except ValueError as error:
    print(f"This is not a valid value {error}")
except ZeroDivisionError as error:
    print(f"Can't divide on 0")
except Exception as error:
    print(f"Something bad happened - {error}")  # should first understand the error
