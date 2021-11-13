from decouple import config


DATABASE_URL = config("DATABASE_URL", cast=str)

TELEGRAM_BOT_ADMIN_IDS = config("TELEGRAM_BOT_ADMIN_IDS", cast=str).split(',')
TELEGRAM_BOT_API_TOKEN = config("TELEGRAM_BOT_API_TOKEN", cast=str)
TELEGRAM_USE_REDIS = config("TELEGRAM_USE_REDIS", cast=str)

TABLES_PREFIX = config("TABLES_PREFIX", cast=str)
