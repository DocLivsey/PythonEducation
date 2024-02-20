# Дано натуральное число n. Выведите следующее за ним чётное число.

n = int(input("input n"))
print("next even: " + str(n + (n%2 or 2)))