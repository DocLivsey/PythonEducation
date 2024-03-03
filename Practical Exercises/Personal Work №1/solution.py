# Дано число n. Найти наименьшее число, которое можно получить
# перестановкой цифр числа n и которое является палиндромом.

# 123475321 - NO
# 16321632 - 12366321
# 1362231 - 1236321
# 8912821991 - NO
# 324455423 - NO
# 673619719 - 136799761

def makePalindromeComparisonLists(number):
    numbers_list = [i for i in str(number)]
    first_in_numbers = []
    second_in_numbers = []
    number_bin = []
    for number in numbers_list:
        if number not in first_in_numbers:
            first_in_numbers.append(number)
        elif number in first_in_numbers and number not in second_in_numbers:
            second_in_numbers.append(number)
        else:
            number_bin.append(number)
    return [first_in_numbers, second_in_numbers, number_bin]


def canBePalindrome(number):
    comparison_lists = makePalindromeComparisonLists(number)
    print(comparison_lists)
    print(sorted(comparison_lists[0]), sorted(comparison_lists[1]))
    len_difference_less_than_one = abs(len(comparison_lists[0]) - len(set(comparison_lists[1]))) <= 1
    is_second_set_in_first_list = set(comparison_lists[1]).issubset(comparison_lists[0])
    if sorted(comparison_lists[0]) == sorted(comparison_lists[1]) and len(comparison_lists[2]) == 1:
        return True
    elif is_second_set_in_first_list and len_difference_less_than_one and comparison_lists[2] == []:
        return True
    return False


def makeMinPossiblePalindrome(number):
    if not canBePalindrome(number):
        return "Cant make palindrome at all"
    comparison_lists = makePalindromeComparisonLists(number)
    first_in_numbers = comparison_lists[0]
    second_in_numbers = comparison_lists[1]
    middle_element = ""
    if len(first_in_numbers) == len(second_in_numbers):
        return "".join(first_in_numbers + second_in_numbers)
    elif len(first_in_numbers) > len(second_in_numbers):
        middle_element = str(set(first_in_numbers).difference(second_in_numbers)).strip("{}")
    elif len(first_in_numbers) < len(second_in_numbers):
        middle_element = str(set(second_in_numbers).difference(first_in_numbers)).strip("{}")
    first_in_numbers.remove(middle_element[1])
    first_in_numbers.sort()
    second_in_numbers.sort(reverse=True)
    return "".join(first_in_numbers + list(middle_element[1]) + second_in_numbers)


print(makeMinPossiblePalindrome(324155423))