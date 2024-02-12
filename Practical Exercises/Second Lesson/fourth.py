# Необходимо узнать, какую оценку получит ученик в четверти. Учитель
# придерживается следующей системы: вычисляется среднее арифметическое всех оценок в
# журнале, и ставится ближайшая целая оценка, не превосходящая среднего
# арифметического.

import math

list_input = list(map(int, input("input list items: ").split()))
avg = 0
count = 0
for i in range(0, len(list_input) - 1):
    if list_input[i] == 2 and list_input[i + 1] != 2:
        i += 1
        count += 1
    elif list_input[i] != 2:
        avg += list_input[i]
    avg += list_input[len(list_input) - 1]

print(math.floor(avg / (len(list_input) - count)))
