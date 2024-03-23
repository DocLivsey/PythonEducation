# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.

with open("text.txt") as input_file:
    text = input_file.read().strip().replace("'", " ").replace(",", " ").replace(".", " ").split()
    words_mapa = {}
    for word in text:
        if word not in words_mapa.keys():
            words_mapa[word] = 1
        else:
            words_mapa[word] += 1
    sortedByValue = sorted(words_mapa.items(), key=lambda x: -x[1])
    max_value = sortedByValue[len(sortedByValue) - 1][1]
    filteredByValues = []
    for i in range(max_value):
        listByValueI = list(filter(lambda x: x[1] == i + 1, sortedByValue))
        filteredByValues.append(listByValueI)
    sortedByKey = []
    for filteredList in filteredByValues:
        filteredList.sort(key=lambda x: x[0])
        for word in filteredList:
            print(word)
input_file.close()
