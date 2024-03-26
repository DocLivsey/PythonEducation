# Дана строка. Нужно извлечь все имена и фамилии из текста.

import re

input_str = ("jr fkj mamnfa Fillimon kfakf Jopa egor fakf\n"
             "wfmw asmfm Vova alfm VAsya msf\n"
             "Danya efawf, qw'lfwf\n"
             "eflw, fl lw, flw qwf Gleb")
pattern = r"^[A-ZА-Я]{1}[a-zа-я]+$"
words = input_str.split()
names = []
for word in words:
    if re.match(pattern, word) is not None:
        names.append(word)
print(names)
