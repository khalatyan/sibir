import pymysql
pymysql.install_as_MySQLdb()
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sibir',
        'USER': 'u1455403_mysql',
        'PASSWORD': '3cwQRTGbAS5Z2wF',
        'HOST': '127.0.0.1',
    }
}


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'e3d9cd450949.ngrok.io', 'dsk-sibir2016.ru', 'www.dsk-sibir2016.ru']

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
