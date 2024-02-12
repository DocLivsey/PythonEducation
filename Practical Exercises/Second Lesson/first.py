# Дан список чисел Выведите все элементы списка с четными индексами (то
# есть A[0], A[2], A[4], ...). В этой задаче нельзя использовать инструкцию if.

list_input = list(map(float, input("input list items: ").split()))
[print(list_input[i]) for i in range(1, len(list_input), 2)]