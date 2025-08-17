import time

age = "35sds"  # will raise an error
age_2 = 35  # always int

while True:
    try:
        age = int(age)
        print(age + 1)
        break
    except ValueError as error:
        print(f"This is not a valid value {error}")
        time.sleep(2)
        age = int(age_2)
        print(age + 1)
        continue
    except ZeroDivisionError as error:
        print(f"Can't divide on 0")
        time.sleep(2)
        continue
    except Exception as error:
        print(f"Something bad happened - {error}")  # should first understand the error
        time.sleep(2)
        continue
