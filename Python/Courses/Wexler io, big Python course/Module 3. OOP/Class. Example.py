class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


captain = Human(first_name="Han", last_name="Solo")
jedi = Human(first_name="Luke", last_name="SkyWalker")

# How to read class data
print(captain.first_name)

name = input("Enter name")
surname = input("Enter surname")

person = Human(name, surname)
print(person.last_name + " " + person.last_name)


