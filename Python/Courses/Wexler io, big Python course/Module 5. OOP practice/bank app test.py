class Customer:
    def __init__(self, first_name: str, last_name: str, passport_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

    def __repr__(self):  # для удобного вывода
        return f"Customer({self.first_name} {self.last_name}, {self.passport_number})"

    def __str__(self):
        return f"Customer({self.first_name} {self.last_name}, {self.passport_number})"


class Bank:
    def __init__(self): # variables
        # self.customers = list()  # can use self. syntax even with no parameters. O(N)
        self.customers = dict()  # can use self. syntax even with no parameters. O(1), unique keys

    def add_customer(self, first_name: str, last_name: str, passport_number: int):
        # self.customers.append(Customer(first_name, last_name, passport_number)) # O(N)
        self.customers.get(passport_number, Customer(first_name, last_name, passport_number)) # O(1)

        # ?? this lines adds a new entry, adding key as first value:
        # {12345: Customer(John Smith, 12345)}
        self.customers[passport_number] = Customer(first_name, last_name, passport_number)

    def get_customer(self, passport_number: int):
       # for cust in self.customers:
           # Why it works: [Customer("John", "Smith", 12345)], NOT ["John", "Smith", 12345]
           # O(N) or redundant - for large lists
           # if cust.passport_number == passport_number:
           #     return cust

           # Same but for dict. O(1), unique keys
       if passport_number not in self.customers:
           raise KeyError(f"Клиент с паспортом {passport_number} не найден")
       return self.customers.get(passport_number)



bank = Bank()
bank.add_customer(first_name="John", last_name="Smith", passport_number=12345)
print(f'Added customer {bank.customers}')
customer = bank.get_customer(12345)
print(customer)
# customer = bank.get_customer(2313)
# print(customer)


