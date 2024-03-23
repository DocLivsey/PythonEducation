# Выведите все строки данного входного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

with open("input4.txt") as input_file:
    all_lines = input_file.readlines()
    reversed_lines = sorted(all_lines, reverse=True)
    for line in reversed_lines:
        print(line)
input_file.close()