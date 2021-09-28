# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u1455403_sibir',
        'USER': 'u1455403_sibir',
        'PASSWORD': 'pA8yN8cA7zxT4x',
        'HOST': 'localhost',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'e3d9cd450949.ngrok.io', 'dsk-sibir2016.ru', 'www.dsk-sibir2016.ru']

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
<<<<<<< HEAD
        
=======
        
>>>>>>> 3ff7dd8d8c009b3756539d98d3637ce1c7d1b3a7
