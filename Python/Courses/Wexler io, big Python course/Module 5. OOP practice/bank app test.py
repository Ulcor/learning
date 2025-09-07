class Customer:
    def __init__(self, first_name: str, last_name: str, passport_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

class Bank:
    def __init__(self):
        self.customers = list()