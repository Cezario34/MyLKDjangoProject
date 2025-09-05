from .base import *

# Продакшн
DEBUG = False

# В prod обязательно задай домены в .env
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Безопасность/HTTPS (поднимешь когда будет прокси/сертификат)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Статика/медиа (примерные пути; адаптируй под свой деплой)
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"

# БД из переменной окружения (когда перейдёшь на Postgres)
# Пример (оставь, если используешь SQLite на dev):
# DATABASES = {
#     "default": env.dj_db_url("DATABASE_URL")  # если решишь подключить dj-database-url
# }
