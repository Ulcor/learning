class Car:
    pass             # pass - это способ в Питоне не делать ничего


class Mercedes(Car):
    def __init__(self):
        super().__init__()  # инициализируем родителя
        self.country = "Germany"


class A(Mercedes):
    def __init__(self):
        super().__init__()
        self.price = "low"


class S(Mercedes):
    def __init__(self):
        super().__init__()
        self.price = "high"
        self.comfort = "maximum"


class Maybach(S):
    def __init__(self):
        super().__init__()
        self.price = "infinite"
        self.has_champagne_fridge = True


car = Maybach()

print(car.country)   # Germany - из класса Mercedes
print(car.price)     # infinite - из класса Maybach
print(car.comfort)   # maximum - из класса S
print(car.has_champagne_fridge) # True из класса Maybach