# Дан список, состоящий из нечётного числа элементов, при этом все элементы
# различны. Найти медиану списка: элемент, который стоял бы ровно посередине списка,
# если список отсортировать. (При решении этой задачи нельзя модифицировать данный
# список (в том числе и сортировать его), использовать вспомогательные списки.)

list_input = list(map(float, input("input list items: ").split()))
median: float = 0
for i in list_input:
    more_count = 0
    less_count = 0
    for j in list_input:
        if i > j:
            less_count+=1
        elif i < j:
            more_count+=1
    if less_count == more_count:
        median = i
        break

print(i, sorted(list_input))