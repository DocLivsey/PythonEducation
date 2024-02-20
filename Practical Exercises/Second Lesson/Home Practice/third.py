# Дан список чисел. Определите, сколько в этом списке элементов, которые
# больше двух своих соседей и выведите количество таких элементов.

list_input = list(map(float, input("input list items: ").split()))
[print(list_input[i]) for i in range(1, len(list_input) - 1) if list_input[i] > list_input[i+1] and list_input[i] > list_input[i-1] ]