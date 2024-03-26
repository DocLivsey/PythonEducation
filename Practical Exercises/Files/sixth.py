# Выведите в обратном порядке содержимое всего файла полностью.
# Для этого считайте файл целиком при помощи метода read() .

with open("input6.txt") as input_file:
    text = input_file.read().split()
    print(text)
    reversed_text = list(reversed(text))
    print(reversed_text)
input_file.close()