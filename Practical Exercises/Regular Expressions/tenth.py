# Написать регулярное выражение для извлечения из текста всех email-адресов.

import re

pattern = r'^[A-Za-z0-9+_.-]+@{1}[A-Za-z]+.[a-z]+$'
text = ("aas@mail.ru"
        "kfarfsmail.com.ru"
        "@@gmail.com"
        "wfkwmf@@.ru"
        "kwef@@skfkaw"
        ".ru@.com")
mails = []
for word in text:
    if re.match(pattern, word) is not None:
        mails.append(word)
print(mails)
