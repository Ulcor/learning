class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(f'{self.first_name} {self.last_name}')


object = Human(first_name="Luke", last_name="Skywalker")
object.print_name()

customer = Human(first_name="John", last_name="Doe")
apple_ceo = Human(first_name="Tim", last_name="Cook")

customer.print_name()
apple_ceo.print_name()
