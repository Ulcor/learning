def my_decorator(f):    # f - это декорируемая функция
    def wrap(*args, **kwargs):
        # args - это список принимаемых обязательных параметров
        # kwargs - это dict с опциональными параметрами

        # здесь ВАША дополнительная логика ДО выполнения функции
        result = f(*args, **kwargs)  # вызвали декорируемую функцию с входными параметрами
        # здесь ВАША дополнительная логика ПОСЛЕ выполнения функции
        return result
    return wrap


# Example
def log_function(f):
    def wrap(*args, **kwargs):
        print(f'Вызываем функцию {f}')
        print(f'Входные параметры {args}')
        print(f'Опциональные параметры {kwargs}')
        result = f(*args, **kwargs)
        print(f"Результат вызова функции {result}")
        return result
    return wrap

@log_function
def greetings(name):
    print(f"Hello, {name}")

greetings("Harry") # will print all decorator stuff


# Same for the class object
@log_function
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