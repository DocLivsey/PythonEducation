# Дано количество названий столиц и государств (число N).
# В следующих N строках  задаются  названия  столиц  и  государств.
# Отсортировать названия  столиц  и государств по названию государства в лексикографическом порядке.

# Ввод              Вывод
# 2
# Moscow Russia     Vienna Austria
# Vienna Austria    Moscow Russia

N = int(input("input count = "))
mapa = {}
for i in range(N):
    words_pair = input("input capital and country: ").split(" ")
    mapa[words_pair[0]] = words_pair[1]
print(str(sorted(list(mapa.items()), key=lambda x: x[1])[0]).strip("()"))
