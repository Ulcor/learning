class Animal:
    def __init__(self):
        pass
    def walk(self):
        return f"Animal {classmethod} is walking"


    def say(self):
        return "???"


class Cat(Animal):
    def say(self):
        return "Meouw"


class Dog(Animal):
    def say(self):
        return "Woof"