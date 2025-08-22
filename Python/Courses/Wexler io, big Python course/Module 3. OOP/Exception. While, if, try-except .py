import time
import os

age = "35sds"  # will raise an error
age_2 = 35  # always int
my_path = 'Python/Courses/Wexler io, big Python course/Module 3. OOP/test_file.csv'

while not os.path.exists(my_path):
    try:
        print("Waiting for file 'test_file.csv' in the same directory")
        file = open(my_path)
        print(file.read())
        file.close()
        break
    except FileNotFoundError as error:
        print(f"This is not a valid value {error}")
        time.sleep(2)
        age = int(age_2)
        print(age + 1)
