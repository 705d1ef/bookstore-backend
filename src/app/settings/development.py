from app.settings.base import *

DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]


MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
MIDDLEWARE.insert(1, "debug_toolbar_force.middleware.ForceDebugToolbarMiddleware")


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DEBUG_HOST"),
        "PORT": env("DB_PORT"),
    }
}
