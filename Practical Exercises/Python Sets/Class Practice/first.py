# . Дан список чисел. Определить, сколько в нем
# встречается различных чисел. Вывести эти числа

input_list = set(map(str, input("input items: ").strip().split()))
print(len(input_list))