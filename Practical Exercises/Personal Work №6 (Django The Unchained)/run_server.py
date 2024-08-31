import os
import sys

# Отключаем автоперезагрузку Django
os.environ['DJANGO_AUTORELOAD_DEBUG'] = 'false'

# Добавляем путь к директории mysite
sys.path.append(os.path.abspath('mysite'))

# Устанавливаем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# Импортируем WSGI-приложение
from django.core.wsgi import get_wsgi_application

# Получаем WSGI-приложение
application = get_wsgi_application()

# Запускаем сервер с использованием WSGI
from wsgiref.simple_server import make_server

# Указываем адрес и порт
server = make_server('127.0.0.1', 8000, application)
print("Serving on http://127.0.0.1:8000/")
server.serve_forever()