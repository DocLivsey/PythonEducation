# Дана строка, состоящая только из строчных латинских букв.
# Определить, какое наименьшее число букв нужно дописать
# к этой строке справа так, чтобы она стала палиндромом.

input_string = input("input string = ")
while input_string.lower() == input_string.upper():
    print("Error! there is not a letter in string")
    input_string = input("input string = ")

# agfdsdf

indexToCopyTo: int = len(input_string) - 1
moveIndexOn: int = 0

for i in range(len(input_string) - 1):
    if input_string[i] != input_string[-1]:
        continue
    else:
        if input_string[i:] == input_string[-1:i - 1:-1]:
            indexToCopyTo = i
            i = len(input_string) - 1
print(indexToCopyTo)