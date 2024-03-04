# Дана строка. Найти слово, которое в этой строке встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом (алфавитном) порядке.

# Ввод  apple orange banana banana orange
# Вывод  banana

str_list = input("input string: ").split(" ")
mapa = {}
for i in str_list:
    if i not in mapa.keys():
        mapa[i] = 1
    else:
        mapa[i] += 1
sortedByValues = sorted(list(mapa.items()), key=lambda x: x[1], reverse=True)
filteredByValues = list(filter(lambda x: x[1] == sortedByValues[0][1], sortedByValues))
sortedByKeys = sorted(filteredByValues)
print(sortedByKeys[0])