# Вводится последовательность строк.
# В каждой строке нужно поменять
# местами две первые буквы в каждом слове,
# состоящем из двух и более букв.

import re

input_str = "faskk asmfkmsk s g sfmkakfm asmfkm \nasnfasnfnsfsfff sfa f s \nfr e x l asf"
pattern = r"[A-Za-zА-Яа-я]{2,}"
lines = input_str.split('\n')
new_str = ""
for line in lines:
    words = line.split()
    for i in range(len(words)):
        if re.match(pattern, words[i]) is not None:
            word = list(words[i])
            word[0], word[1] = word[1], word[0]
            words[i] = "".join(word)
        new_str += words[i] + " "
    new_str += "\n"
print(new_str)
