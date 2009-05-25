DEBUG = False

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = '$$$$PROJECT_NAME$$$$-dev'
DATABASE_USER = '$$$$PROJECT_NAME$$$$'
DATABASE_PASSWORD = 'blah'
DATABASE_HOST = '$$$$DEV_DATABASE_HOST$$$$'
DATABASE_PORT = ''

MEDIA_URL = 'http://media-$$$$DEV_APP_HOST$$$$/'
ADMIN_MEDIA_PREFIX = 'http://media-$$$$DEV_APP_HOST$$$$/admin/'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'