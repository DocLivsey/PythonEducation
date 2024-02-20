# Дано два натуральных числа  A и B (A⩽B)
# вывести все чётные числа на отрезке от A до B
# (Без использования условного оператора if).

a = int(input("input a: "))
b = int(input("input b: "))

for i in range(a, b + 1, 2):
    print(i+(i%2))