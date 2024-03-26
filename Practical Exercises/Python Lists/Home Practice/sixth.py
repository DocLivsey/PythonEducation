# Дан список целых чисел. Развернуть элементы с нечетными индексами.

list_input = list(map(int, input("input list items: ").split()))
for i in range(0, len(list_input) // 2, 2):
    list_input[i], list_input[-i - 1] = list_input[-i - 1], list_input[i]
print(list_input)