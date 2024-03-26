# Дан текст на языке племени Мумба-Юмба. Выведите все слова,
# встречающиеся в тексте, разделяя их пробелом.
# Слова должны быть отсортированы  по  убыванию  их  количества  появления  в  тексте,
# а  при одинаковой частоте появления — в алфавитном порядке.

with open("input3.txt") as input_file:
    text = input_file.read().strip().split()
    words_mapa = dict()
    for word in text:
        if word not in words_mapa.keys():
            words_mapa[word] = 1
        else:
            words_mapa[word] += 1
    sorted_words = sorted([(k, v) for (v, k) in words_mapa.items()], reverse=True)

input_file.close()

with open("output3.txt", "w") as output_file:
    for key_value in sorted_words:
        output_file.write("".join(str(key_value)))
output_file.close()