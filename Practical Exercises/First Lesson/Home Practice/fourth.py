# Сколько дней будет длится маршрут длиной m километров,
# если машина каждый день проезжает n километров?

m = int(input("input km: "))
n = int(input("input km per days: "))

print("days count: " + str(m//n + (m%n)))