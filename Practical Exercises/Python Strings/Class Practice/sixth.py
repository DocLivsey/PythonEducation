# Известна задача, в которой требуется продолжить числовой ряд:
# 1 11 21 1211 111221 312211 13112221 1113213211 ...
# Выведите одно число - k-е число в этом ряду


# using the regular expression
import re
a = "<<<VVV>>>VVV"
res = [x[0] for x in re.findall(r"((.)\2*)", a)]

k = int(input("input k = "))
previous: str = "1"
next: str = ""

for _ in range(k):
    last_item = previous[0]
    repeatingItems = []
    items = ""
    for item in previous:
        if item == last_item:
            items += item
        else:
            repeatingItems.append(items)
            items = item
            last_item = item
    repeatingItems.append(items)

    for item in repeatingItems:
        next += str(len(item)) + item[0]
    previous = next
    print(next)
    next = ""
