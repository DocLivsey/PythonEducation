# Дана строка. Получить первое слово из строки
# Дана строка. Получить последнее слово из строки

import re

input_str = input("input string: ")
input_str = re.findall('[A-Za-z]*', input_str)
print(input_str)
print(input_str[0])
print(input_str[-1])
