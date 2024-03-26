# Дана строка. Для каждого слова найти, сколько раз оно встречалось ранее
# Ввод  one two one tho three
# Вывод  0 0 1 0 0

string = input("input string: ").split(" ")

mapa = {}
for i in string:
    if i not in mapa.keys():
        mapa[i] = 0
    else:
        mapa[i] += 1