# Дана строка, содержащая буквы латинского алфавита,
# пробелы, запятые и точки.
# Отформатировать этот текст по следующим правилам:
# 1) В начале и конце строки не должно быть пробелов.
# 2) Все слова разделяются ровно одним пробелом.
# 3) Точки и запятые пишутся слитно с предыдущим словом, после знака
# препинания ставится пробел.

str = input("input string: ").strip()
str = " ".join(str.split())
str = str.replace(" ,", ", ").replace(",", ", ")
str = str.replace(".", ". ").replace(" .", ". ")
print(str)