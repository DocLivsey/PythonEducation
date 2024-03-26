# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Программа получает на вход количество стран N. Далее идет N строк,
# каждая строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Ввод                                      Вывод
# 2                                         Austria Russia Russia
# Russia Moscow Petersburg Novgorod Kaluga
# Austria Vienna Salzburg Innsbruck

# 3
# Salzburg Moscow Novgorod

N = int(input("input count = "))
mapa = {}
for i in range(N):
    words_pair = input("input country and cities: ").split(" ")
    mapa[words_pair[1]] = words_pair[0]
input_s: str = input("input city name: ")
cities = []
while "end" not in input_s:
    cities.append(input_s)
    input_s = input("input city name: ")
for city in cities:
    if city in mapa.keys():
        print(mapa[city])
    else:
        print("there is no city named: ", city)
