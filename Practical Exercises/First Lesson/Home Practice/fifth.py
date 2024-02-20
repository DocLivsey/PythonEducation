# Дано два натуральных числа a и b. Найти наибольшее значение из них.

a = int(input("input a : "))
b = int(input("input b : "))

print((a>b)*a or b*(b>=a))