# Проверка входных данных. Напишите декоратор validate_input,
# который будет  проверять  входные  данные  функции  на  соответствие  заданному условию.
# Если  данные  не  проходят  проверку,  должно  выбрасываться исключение.
# Пример использования и ожидаемый вывод:
# @validate_input(lambda x: x > 0, "Введите положительное число")
# def calculate_square(x):
# return x * x
# calculate_square(5)
# # Ожидаемый вывод: 25
# calculate_square(-2)
# # Ожидаемое исключение: ValueError("Введите положительное число")

def validate_input(validate_func, comment):
    def decorator(func):
        def wrapper(*args):
            if validate_func(*args):
                return func(*args)
            else:
                raise ValueError(comment)
        return wrapper
    return decorator


@validate_input(lambda x: x > 0, "Введите положительное число")
def calculate_square(x):
    return x * x


print(calculate_square(2))
