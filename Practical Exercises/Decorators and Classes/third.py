# Замедление  работы  функции.
# Напишите  декоратор slow_down,
# который замедляет выполнение функции на заданное количество секунд (использовать модуль time).
# Пример использования и ожидаемый вывод:
# @slow_down(2)
# def count_down(n): while n > 0:
# print(n) time.sleep(1) n -= 1
# print("Старт!") count_down(3)
# # Вывод: # 3
# # 2
# # 1
# # Старт!

import time


def slow_down(slow_time):
    def decorator(func):
        time.sleep(slow_time)
        return func

    return decorator


@slow_down(10)
def count_down(n):
    while n > 0:
        print(n)
        n -= 1
    print("start")


count_down(5)