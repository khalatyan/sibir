import os, sys
sys.path.insert(0, '/var/www/u1455403/data/www/dsk-sibir2016.ru/sibir')
sys.path.insert(1, '/var/www/u1455403/data/.env/lib/python3.7.0/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'sibir.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
