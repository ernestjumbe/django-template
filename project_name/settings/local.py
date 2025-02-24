from .base import *
from .secrets import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
    "django_extensions",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("AFROURBAN_SQL_ENGINE", ""),
        "NAME": os.environ.get("AFROURBAN_SQL_DATABASE", "afrourban"),
        "USER": os.environ.get("AFROURBAN_SQL_USER", "afrourban"),
        "PASSWORD": os.environ.get("AFROURBAN_SQL_PASSWORD", "password"),
        "HOST": os.environ.get("AFROURBAN_SQL_HOST", "localhost"),
        "PORT": os.environ.get("AFROURBAN_SQL_PORT", 5432),
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

HTML_MINIFY = False

EMAIL_HOST = "email"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 1025
EMAIL_USE_TLS = False


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    "INSERT_BEFORE": "</head>",
    "RENDER_PANELS": True,
}
