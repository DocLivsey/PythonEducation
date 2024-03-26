# Во входной строке записана последовательность чисел через пробел. Для каждого
# числа определить, встречалось ли это число ранее в последовательности или нет.
# Ввод Вывод
# 1 2 3 2 3 4 NO
#             NO
#             NO
#             YES
#             YES
#             NO

input_list = list(map(int, input("input items: ").strip().split()))
s: set = set()
length = 0
for i in input_list:
    s.add(i)
    if len(s) > length:
        length = len(s)
        print("No")
    else:
        print("Yes")
