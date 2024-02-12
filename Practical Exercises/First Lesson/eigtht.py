a = int(input("input a: "))
b = int(input("input b: "))

for i in range(a, b + 1, 2):
    print(i+(i%2))