# Дано   натуральное   число n. Найти   сумму 1!+2!+3!+...+n!.
# (С использованием только одного цикла).

n = int(input("input n = "))
factorialSum: float = 0
factorial: float = 1
for i in range(1, n + 1):
    factorial *= i
    factorialSum += factorial

print("Σn! = ", factorialSum)