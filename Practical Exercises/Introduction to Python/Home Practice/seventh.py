# Дано два натуральных числа N и M.
# Петя стоит на поле размером N×М метров на  расстоянии x метров  от одной из длинных  сторон
# (не обязательно от ближайшей) и y метров от одной из коротких сторон.
# Какое минимальное расстояние должен пройти Петя, чтобы дойти до края поля?
# Изначально неизвестно, какая сторона является длинной.
import math

N: int = int(input("input N = "))
M: int = int(input("input M = "))
x: int = int(input("input x = "))
y: int = int(input("input y = "))

minDist: float = max(N, M)
points: list = [(0, 0), (0, N), (M, 0), (M, N)]

for point in points:
    minDist = min(minDist, math.sqrt(math.pow((x - point[0]), 2) + math.pow((y - point[1]), 2)))
print(minDist)