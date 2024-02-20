# Необходимо узнать, какую оценку получит ученик в четверти. Учитель
# придерживается следующей системы: вычисляется среднее арифметическое всех оценок в
# журнале, и ставится ближайшая целая оценка, не превосходящая среднего
# арифметического.

import math

list_input = list(map(int, input("input list items: ").split()))
avg = 0
count = 0
for i in range(0, len(list_input) - 2):
    if list_input[i] == 2 and list_input[i + 1] != 2:
        avg += list_input[i + 1]
        count += 1
        i += 1
    elif list_input[i] != 2:
        avg += list_input[i]
        count += 1
        i += 1
avg += list_input[len(list_input) - 1]
count += 1

print(math.floor(avg / count), count, avg)
