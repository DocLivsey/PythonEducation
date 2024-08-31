import os
import sys

sys.path.append(os.path.abspath('mysite'))

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.core.management import execute_from_command_line

execute_from_command_line(["manage.py", "runserver"])
