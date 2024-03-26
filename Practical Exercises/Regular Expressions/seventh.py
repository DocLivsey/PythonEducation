# Дана строка. Вывести слова, состоящие из двух одинаковых слогов.

import re

input_string = "вода вор узел козел ковер провод"
words = input_string.split()
broken_by_syllables = {}
for word in words:
    syllables = []
    for i in range(0, len(word), 2):
        syllables.append(word[i:i+2])
    broken_by_syllables[word] = syllables
matching_words = {}
for syllables in broken_by_syllables.values():
    for syllable in syllables:
        pattern = r"[A-Za-zА-Яа-я]*" + syllable + "[A-Za-zА-Яа-я]*"
        matching_words[syllable] = re.findall(pattern, input_string)
print(matching_words)
