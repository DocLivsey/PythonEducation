# Даны пары слов. Каждое слово является синонимом к парному ему слову.
# Все слова различны. Для одного заданного слова определите его синоним.
# Программа получает на вход количество пар синонимов N. Далее следует N строк,
# каждая строка содержит ровно два слова-синонима. После этого следует одно слово.

N = int(input("input count = "))
mapa = {}
for i in range(N):
    words_pair = input("input pair of words: ").split(" ")
    mapa[words_pair[0]] = words_pair[1]
word = input("input word: ")
if word in mapa.keys():
    print(mapa[word])
else:
    if word not in mapa.values():
        print("there are not synonyms for ", word)
    else:
        synonyms = list(filter(lambda x: x[1] == word, mapa.items()))
        print(synonyms[0][0])

