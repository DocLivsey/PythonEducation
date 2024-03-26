# Дан список чисел Выведите все четные элементы списка.

list_input = list(map(float, input("input list items: ").split()))
[print(x) for x in list_input if x%2==0]