# Дана последовательность строк. Нужно вывести те,
# в которых «кот» встречается в качестве отдельного слова.

import re

lineList = ["jfnlfm", 'ekfmkwemfkmf', 'cat', 'кот', 'кот кот', 'коткоткот']
for line in lineList:
    cat = re.search(r'кот', line)
    if cat is not None:
        print(line)
