import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ws7lj2w&0^-od7zbbpcwlacb0(1j61*ly5g!8ibggtew_frqoi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dsk-sibir2016.ru', 'www.dsk-sibir2016.ru']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'filer',
    'easy_thumbnails',
    'reversion',
    'compressor',
    'adminsortable2',
    'mailer',
    'ckeditor',
    'ckeditor_uploader',

    'core',
    'seo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'removewww.middleware.RemoveWwwMiddleware',
]

ROOT_URLCONF = 'sibir.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'core.context_processor.global_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'sibir.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u2681698_default',
        'USER': 'u2681698_default',
        'PASSWORD': 'GqCtm18GIz3tLw8T',
        'HOST': 'localhost',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Irkutsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

FILE_UPLOAD_MAX_MEMORY_SIZE = 200000000
FILE_UPLOAD_PERMISSIONS = 0o644

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
        
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'compressor.finders.CompressorFinder',
)


EMAIL_BACKEND = "mailer.backend.DbBackend"

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_ALIASES = {
    '': {
        'slider_item_300x168_no_crop': {'size': (300, 168), 'crop': False},
        'news_item_200x200': {'size': (200, 200), 'crop': True},
        'news_item_300x168': {'size': (300, 168), 'crop': True},
        'news_item_300x300': {'size': (300, 300), 'crop': True},
        'news_item_600x300': {'size': (600, 300), 'crop': True},
        'map_marker_marker': {'size': (48, 48), 'crop': True},
        'map_marker_icon': {'size': (50, 100), 'crop': True},
        'slider_item_admin': {'size': (300, 150), 'crop': True, 'quality': 100},
        'slider_item_desktop_thumbnail_lazy': {'size': (1920, 720), 'crop': True, 'quality': 50},
        'slider_item_mobile_thumbnail_lazy': {'size': (400, 600), 'crop': True, 'quality': 50},
        'slider_item_desktop': {'size': (2560, 1038), 'crop': False},
        'slider_item_about': {'size': (800, 600), 'crop': True},
        'slider_item_mobile': {'size': (500, 350), 'crop': True},
        'slider_item_thumbline': {'size': (500, 500), 'crop': False},
        'slider_item_admin': {'size': (300, 168), 'crop': False},
        'service_admin': {'size': (270, 100), 'crop': True, 'quality': 100},
        'service_thumbnail': {'size': (540, 200), 'crop': True, 'quality': 100},
        'service_thumbnail_lazy': {'size': (135, 50), 'crop': True, 'quality': 50},
        'portfolio_image': {'size': (1500, 1500), 'crop': False, 'quality': 100},
        'portfolio_image_thumbnail': {'size': (500, 500), 'crop': True, 'quality': 100},
        'portfolio_image_thumbnail_lazy': {'size': (125, 125), 'crop': True, 'quality': 50},
        'product_admin': {'size': (375, 150), 'crop': True, 'quality': 100},
        'product_thumbnail': {'size': (1500, 600), 'crop': True, 'quality': 100},
        'product_thumbnail_lazy': {'size': (375, 150), 'crop': True, 'quality': 100},
    },
}


# django-ckeditor

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT

CKEDITOR_CONFIGS = {
    'default': {
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Maximize', '-', 'Source', '-', 'autoFormat', 'CommentSelectedRange', 'UncommentSelectedRange'],
            ['PasteText'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['insert', 'Image', 'Table', 'Format'],
        ],
        'height': 150,
        'width': 800,
        'extraPlugins': ','.join(
            [
                'autogrow',
                'sourcedialog',
            ]),

    },
}

# django-removewww

REMOVE_WWW = True

# from sibir.local_settings import *
