import os
from decouple import config
from unipath import Path
import dj_database_url
import django_heroku


BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True


ALLOWED_HOSTS = config("ALLOWED_HOSTS")
INSTALLED_APPS = [
    "adminlte3",
    "adminlte3_theme",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blogapp",
    "ckeditor",
    "ckeditor_uploader",
    "crispy_forms",
]
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    "default": {
        "height": 250,
        "width": 750,
        "config.entities": False,
        "config.htmlEncodeOutput": False,
        "config.basicEntities": False,
    },
}
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "core.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
SESSION_ENGINE = "core.session_backend"


def get_cache():
    import os

    try:
        servers = os.environ["MEMCACHIER_SERVERS"]
        username = os.environ["MEMCACHIER_USERNAME"]
        password = os.environ["MEMCACHIER_PASSWORD"]
        return {
            "default": {
                "BACKEND": "django_bmemcached.memcached.BMemcached",
                # TIMEOUT is not the connection timeout! It's the default expiration
                # timeout that should be applied to keys! Setting it to `None`
                # disables expiration.
                "TIMEOUT": None,
                "LOCATION": servers,
                "OPTIONS": {
                    "username": username,
                    "password": password,
                },
            }
        }
    except:
        return {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}


CACHES = get_cache()


ROOT_URLCONF = "core.urls"
LOGIN_URL = "/login"
LOGOUT_REDIRECT_URL = "index"
TEMPLATE_DIR_CORE = os.path.join(CORE_DIR, "core/templates")
TEMPLATE_DIR_APP = os.path.join(CORE_DIR, "blogapp/templates/blogapp")


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR_CORE, TEMPLATE_DIR_APP],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

DATABASE_URL = os.environ.get("DATABASE_URL")
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES["default"].update(db_from_env)
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Ho_Chi_Minh"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
CRISPY_TEMPLATE_PACK = "bootstrap4"

STATICFILES_DIRS = (os.path.join(CORE_DIR, "core/static"),)
django_heroku.settings(locals())
