# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
# Выведите три найденных числа. Словом считается последовательность больших и маленьких латинских букв
# (для проверки того, состоит ли строка только  из  латинских  букв  удобно  пользоваться  методом  isalpha()).
# Все остальные символы считаются разделителями слов .

with open("input5.txt") as input_file:
    text = input_file.readlines()
    line_text = ''
    for line in text:
        line.replace("`", " ")
        line_text += line
    lines_count = len(text)
    letters = [letter for line in text for letter in line if letter.isalpha()]
    letters_count = len(letters)
    for char in line_text:
        if not char.isalpha():
            line_text.replace(char, " ")
    words = line_text.strip().split()
    words_count = len(words)
    print(f"letters = {letters_count}, words = {words_count}, lines = {lines_count}")
input_file.close()