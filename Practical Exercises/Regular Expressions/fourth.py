# Вводится последовательность строк. Нужно вывести строки,
# в которых фрагмент «кот» присутствует в качестве подстроки не менее 2 раз.

import re

lineList = ["jfnlfm", 'ekfmkwemfkmf', 'cat', 'кот', 'кот кот', 'коткоткот']
for line in lineList:
    cat = re.findall(r'кот', line)
    if len(cat) >= 2:
        print(cat)
