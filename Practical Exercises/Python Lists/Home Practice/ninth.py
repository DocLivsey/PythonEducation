# Найти наибольшую сумму чисел в подпоследовательности заданной длины.
# Дано: список чисел, длина подпоследовательности, для которой нужно найти наибольшую сумму.
#
# Пример
# 3 2 5 4 3 2 4
# 3

list_input = list(map(float, input("input list items: ").split()))
length = int(input("input length of sublist: "))

maxSumOfSubLists: float = 0
for i in range(0, len(list_input) - length + 1):
    sum: float = 0
    for j in list_input[i:i+length]:
        sum += j
    maxSumOfSubLists = max(sum, maxSumOfSubLists)
    print(list_input[i:i+length], sum)
print(maxSumOfSubLists)