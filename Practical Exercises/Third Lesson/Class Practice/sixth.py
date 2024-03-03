# Известна задача, в которой требуется продолжить числовой ряд:
# 1 11 21 1211 111221 312211 13112221 1113213211 ...
# Выведите одно число - k-е число в этом ряду

k = int(input("input k = "))
previous: str = "111233"
next: str = ""
index: int
for i in range(0, len(previous)):
    count: int = 0
    for j in range(0, len(previous)):
        if previous[i] == previous[j]:
            count += 1
        print(i, j, count)
    print(previous[i], count, previous)