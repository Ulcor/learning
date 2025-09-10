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
        self.accounts = dict()

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

    def add_account(self, account, customer):
        self.accounts[customer] = account

    def get_customer_account(self, passport_number: int):
        customer = self.get_customer(passport_number)
        if customer not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[customer]

    def deposit(self,passport_number, amount):
        number = self.get_customer_account(passport_number)
        BankAccount.deposit(number, amount)

    def withdraw(self, passport_number, amount):
        number = self.get_customer_account(passport_number)
        BankAccount.withdraw(number, amount)

class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def __str__(self):   # Also a Method. returns a formatted path
        return f"Your number is {self.number}, amount is {self.amount} currency {self.amount}"

    def deposit(self, value):
        if value:
            # print(f"User {self.number} have credited {value}")
            self.amount = self.amount + value
            # print(f"Total amount is {self.amount} {self.currency}")

    def withdraw(self, value):
        self.amount = self.amount - value


# credit_account = BankAccount(number=2151616125251, currency='USD')
# debit_account = BankAccount(number=20919815115516, currency='USD')

# add_funded = BankAccount(number=2151616125251, currency='USD')
# add_funded.deposit(value=150)
# print(add_funded.amount)
#
# add_funded.withdraw(value=140)
# print(add_funded.amount)


bank = Bank()
bank.add_customer(first_name="John", last_name="Smith", passport_number=12345)
print(f'Added customer {bank.customers}')
customer = bank.get_customer(12345)
print(customer)
bank.add_account(account=customer, customer=customer)
account = bank.get_customer_account(12345)
print(account)

######### pouprazniatsia #########

bank = Bank()
# Add user 1
bank.add_customer(first_name="Alex", last_name="Vilgelmovich", passport_number=64321)
customer_1 = bank.get_customer(64321)
# Add user 2
bank.add_customer(first_name="Mark", last_name="Katz", passport_number=23412)
customer_2 = bank.get_customer(23412)

# Add account 1 2
credit_account = BankAccount(number=2151616125251, currency='USD')
debit_account = BankAccount(number=20919815115516, currency='USD')

# Match user 1 = bank account 1
bank.add_account(account=credit_account, customer=customer_1)
bank.add_account(account=debit_account, customer=customer_2)

# Add 100 units of currency to both
bank.deposit(passport_number=64321, amount=100)
bank.deposit(passport_number=23412, amount=100)
print(bank.customers)

# Money
# print(bank.get_customer(23412))
# bank_account = BankAccount(number=2151616125251, currency='USD')
# print(bank.get_customer(23412))