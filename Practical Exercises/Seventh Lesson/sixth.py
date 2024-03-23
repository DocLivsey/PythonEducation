# Проверить формат телефонного номера.
# Номер должен состоять из 11 знаков и начинаться с 7 или 8.
# На вход подается список телефонных номеров.
# Если номер корректный, то следует вернуть Correct, иначе — Incorrect.

import re

correct_number = r"^[78]{1}-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$"
phonesList = ["+7-918-234-12-54", "8948-543-12-43", "8-746-453-64-98", "8-8474-322-12-32"]
for phone in phonesList:
    check = re.match(correct_number, phone)
    if check is not None:
        print(f"phone number: {phone} is correct")
    else:
        print(f"phone number: {phone} is incorrect")
