class Human:  # Super class
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def move(self):
        print(f"{self.first_name} {self.last_name} is walking")


class Driver(Human):  # Child class
    # Pycharm - click "Generate -> Override method init"
    def __init__(self, first_name, last_name, driver_license, age=None):
        super().__init__(first_name, last_name, age)
        self.driver_license = driver_license

    def move(self):
        print(f"{self.first_name} {self.last_name} is driving")  # This is polymorphism 


human = Human('Luke', 'Skywalker')
human.move()  # выведет в консоль "Luke Skywalker is walking"

driver = Driver('Han', 'Solo', 123456)
driver.move()  # теперь выведет в консоль "Han Solo is driving", так как у Driver есть свой move