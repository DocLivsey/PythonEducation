with open("text.txt") as input_file:
    text = input_file.read().strip().split()
    words_mapa = {}
    for word in text:
        if word not in words_mapa.keys():
            words_mapa[word] = 1
        else:
            words_mapa[word] += 1
    sortedByKeyThenByValue = sorted(sorted(words_mapa.items(), key=lambda x: x[0]), key=lambda x: -x[1])
    for word in sortedByKeyThenByValue:
        print(word)
input_file.close()