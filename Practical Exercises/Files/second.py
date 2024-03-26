# Дан файл, каждая строка которого может содержать одно или несколько целых чисел,
# разделенных одним или несколькими пробелами. Вычислите сумму чисел в каждой строке
# и выведите эти суммы через пробел (для каждой строки выводится сумма чисел в этой строке).

with open("input2.txt") as input_file:
    lines = input_file.readlines()
    for line in lines:
        line_list = list(map(int, line.strip().split()))
        line_sum = sum(line_list)
        print(f"list - {line_list}, sum = {line_sum}")
input_file.close()