class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def __str__(self):   # Also a Method. returns a formatted path
        return f"Your number is {self.number}, amount is {self.amount} currency {self.amount}"

    def deposit(self, value):
        if value:
            print(f"User {self.number} have credited {value}")
            self.amount = self.amount + value
            print(f"Total amount is {self.amount} {self.currency}")

    def withdraw(self, value):
        self.amount = self.amount - value


# credit_account = BankAccount(number=2151616125251, currency='USD')
# debit_account = BankAccount(number=20919815115516, currency='USD')

add_funded = BankAccount(number=2151616125251, currency='USD')
add_funded.deposit(value=150)
print(add_funded.amount)

add_funded.withdraw(value=140)
print(add_funded.amount)
