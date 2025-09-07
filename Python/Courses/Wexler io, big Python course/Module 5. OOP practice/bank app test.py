class Customer:
    def __init__(self, first_name: str, last_name: str, passport_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

    def __repr__(self):  # для удобного вывода
        return f"Customer({self.first_name} {self.last_name}, {self.passport_number})"


class Bank:
    def __init__(self): # variables
        self.customers = list()  # can use self. syntax even with no parameters

    def add_customer(self, first_name: str, last_name: str, passport_number: int):
        self.customers.append(Customer(first_name, last_name, passport_number))

    def get_customer(self, passport_number: int):
       for cust in self.customers:
           # Why it works: [Customer("John", "Smith", 12345)], NOT ["John", "Smith", 12345]
           if cust.passport_number == passport_number:
               return cust
       raise KeyError


bank = Bank()
bank.add_customer(first_name="John", last_name="Smith", passport_number=12345)
customer = bank.get_customer(12345)
print(customer)
# customer = bank.get_customer(2313)
# print(customer)


