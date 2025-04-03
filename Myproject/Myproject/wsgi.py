import os
from django.core.wsgi import get_wsgi_application

# Указываем Django на настройки проекта
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myproject.settings")

# Получаем WSGI-приложение
application = get_wsgi_application()
