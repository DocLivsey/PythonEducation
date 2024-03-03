# Дано число n. Найти наименьшее число, которое можно получить
# перестановкой цифр числа n и которое является палиндромом.

# 123475321 - NO
# 16321632 - 12366321
# 1362231 - 1236321
# 8912821991 - NO
# 324455423 - NO
# 673619719 - 136799761

def canBePalindrome(number):
    numbers_list = [i for i in str(number)]
    first_in_numbers = []
    repetition_numbers = []
    for number in numbers_list:
        if number in first_in_numbers:
            repetition_numbers.append(number)
        elif number not in first_in_numbers:
            first_in_numbers.append(number)
    if len(first_in_numbers) == len(repetition_numbers) or len(first_in_numbers) == len(repetition_numbers) + 1:
        return True
    return False


def makeMinPossiblePalindrome(number):
    if not canBePalindrome(number):
        return "Cant make palindrome at all"
    numbers_list = [i for i in str(number)]
    first_in_numbers = []
    repetition_numbers = []
    for number in numbers_list:
        if number in first_in_numbers:
            repetition_numbers.append(number)
        elif number not in first_in_numbers:
            first_in_numbers.append(number)
    first_in_numbers = sorted(first_in_numbers)
    repetition_numbers = sorted(repetition_numbers, reverse=True)
    return "".join(first_in_numbers + repetition_numbers)


print(makeMinPossiblePalindrome(324455423))
