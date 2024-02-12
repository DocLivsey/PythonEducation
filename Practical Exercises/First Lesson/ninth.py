a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))
d = int(input("input d: "))

for i in range(a, b+1):
    print((i%d==c)*i)