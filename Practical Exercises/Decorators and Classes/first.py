# Создание логирования функций.
# Напишите декоратор log_decorator,
# который будет добавлять функциям логирование:
# при вызове функции будет выводиться информация
# о её имени и переданных аргументах.
# Пример использования и ожидаемый вывод:
# @log_decorator
# def multiply(a, b):
# return a * b
# multiply(3, 4)
# #Вызов функции multiply с аргументами (3, 4)


def log_decorator(func):
    def wrapper(*args):
        print(f"Вызов функции {func.__name__} с аргументами {args}")
        return func(*args)
    return wrapper


@log_decorator
def multiply(a, b):
    return a * b


print(multiply(3, 4))
