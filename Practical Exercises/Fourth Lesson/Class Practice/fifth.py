# Есть N школьников, каждый из которых знает определенное количество языков.
# Необходимо определить, какие языки знают все школьники и какие языки знает хотя бы
# один из них.

N: int = int(input("input N = "))
languages: list = []

while N > 0:
    input_list = list(map(str, input("input items: ").strip().split()))
    languages.append(input_list)
    N -= 1
intersect = set(languages[0])
for i in range(1, len(languages)):
    intersect.intersection(set(languages[i]))
print(intersect)