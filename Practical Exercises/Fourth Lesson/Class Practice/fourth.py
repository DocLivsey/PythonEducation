# Дети играют в разноцветные кубики из своих наборов. Они хотят узнать, сколько
# цветов присутствуют в обоих наборах, а сколько у каждого из них уникальных цветов.
# Помогите детям найти ответ на этот вопрос. Вывксти количество цветов и сами цвета

input_list1 = list(map(str, input("input items: ").strip().split()))
input_list2 = list(map(str, input("input items: ").strip().split()))
union = set(input_list1).union(set(input_list2))
intersect = set(input_list1).intersection(set(input_list2))

print(union, len(union))
print(set(input_list1).difference(intersect), len(set(input_list1).difference(intersect)))
print(set(input_list2).difference(intersect), len(set(input_list2).difference(intersect)))