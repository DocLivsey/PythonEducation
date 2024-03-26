# Даны два списка чисел. Найти, сколько чисел
# содержится одновременно в первом
# списке и во втором списке.
# Вывести эти числа в порядке возрастания

input_list1 = set(map(str, input("input items: ").strip().split()))
input_list2 = set(map(str, input("input items: ").strip().split()))

print(len(set(input_list2).intersection(set(input_list1))))
print(list(set(input_list2).intersection(set(input_list1))).sort())
