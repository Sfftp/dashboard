from pathlib import Path
import os
import dotenv
from django.urls import reverse_lazy

__all__ = []

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "super_secret_key")

DEBUG = os.getenv("DJANGO_DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost,*",
).split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_plotly_dash.apps.DjangoPlotlyDashConfig",
    "about.apps.AboutConfig",
    "dashes.apps.DashesConfig",
    "homepage.apps.HomepageConfig",
    "accounts.apps.AccountsConfig",
    "django.contrib.postgres",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


def debug_toolbar_config_ruler(argument):
    return True


if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": debug_toolbar_config_ruler,
        "INSERT_BEFORE": "</head>",
    }


ROOT_URLCONF = "TubikDash.urls"
CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "TubikDash.wsgi.application"

POST_NAME = os.getenv("DB_NAME")
POST_USER = os.getenv("DB_USER")
POST_PASSWORD = os.getenv("DB_PASSWORD")
POST_HOST = os.getenv("DB_HOST", "localhost")
POST_PORT = os.getenv("DB_PORT")

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": POST_NAME,
        "USER": POST_USER,
        "PASSWORD": POST_PASSWORD,
        "HOST": POST_HOST,
        "PORT": POST_PORT,
    },
}

LOGIN_URL = reverse_lazy("accounts:login")
LOGIN_REDIRECT_URL = reverse_lazy("dashes:index")
LOGOUT_REDIRECT_URL = reverse_lazy("accounts:login")

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

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static_dev/"

STATICFILES_DIRS = [
    BASE_DIR.parent / "static_dev",
]

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/users/login/"

LOGIN_REDIRECT_URL = "/"

X_FRAME_OPTIONS = 'SAMEORIGIN'