import os

import jinja2

jinja2_env = jinja2.Environment(
    loader=jinja2.PackageLoader(package_name='src'), trim_blocks=True,
)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

PORT = int(os.getenv('PORT', 0))

TOKEN = os.getenv('TOKEN')

SUPERUSER_ID = int(os.getenv('SUPERUSER_ID'))

JIGASYA_CHAT_ID = int(os.getenv('JIGASYA_CHAT_ID'))

DATABASE_URL = os.getenv('DATABASE_URL', '')
# sqlalchemy doesn't support postgres driver
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres', 'postgresql', 1)

REDIS_URL = os.getenv('REDIS_URL')
