import cgi

form = cgi.FieldStorage()
first_name = form.getfirst("FirstName", "не задано")
last_name = form.getfirst("SurName", "не задано")
passport = form.getfirst("Passport", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>Обработка Клиентов </title> 
        </head>
        <body>""")
print("<h1>Обработка Клиентов</h1>")
print("<p>Имя: {}</p>".format(first_name))
print("<p>Фамилия: {}</p>".format(last_name))
print("<p>Паспорт: {}</p>".format(passport))
print("""</body> 
</html>""")
