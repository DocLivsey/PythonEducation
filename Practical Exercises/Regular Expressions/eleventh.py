#  Большинство адресов состоит из трёх частей: название улицы, номер дома и номер квартиры.
#  Название улицы может состоять из нескольких слов, каждое из которых пишется с заглавной буквы.
#  Номер дома может содержать после себя букву.
# Перед названием улицы может быть написано «Улица», «улица», «Ул.» или «ул.»,
# перед номером дома — «дом» или «д.», перед номером квартиры — «квартира» или «кв.».
# Также номер дома и номер квартиры могут быть разделены дефисом без пробелов.
# Дан текст, в нём нужно найти все адреса и вывести их в виде «Пушкина 32-135».
# Для упрощения мы не будем учитывать дома, которые находятся не на улицах,
# а на площадях, набережных, бульварах и так далее.

import re

pattern = r''
with open("input.txt", "r") as input_file:
    text = input_file.readlines()
    print(text)
