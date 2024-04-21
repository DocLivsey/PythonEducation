import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("FirstName", "не задано")
text2 = form.getfirst("SurName", "не задано")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Обработка книг </title> 
        </head>
        <body>""")
print("<h1>Обработка туристов</h1>")
print("<p>Имя: {}</p>".format(text1))
print("<p>Фамилия: {}</p>".format(text2))
print("""</body> 
</html>""")
