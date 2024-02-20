# Дан список чисел. В списке все элементы различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.

list_input = list(set(map(float, input("input list items: ").split())))
print(list_input)

minInd: int = list_input.index(min(list_input))
maxInd: int = list_input.index(max(list_input))

print(list_input)
list_input[minInd], list_input[maxInd] = list_input[maxInd], list_input[minInd]
print(list_input)