import os

from dotenv import load_dotenv

load_dotenv()

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

PORT = int(os.getenv('PORT'))

TOKEN = os.getenv('TOKEN')
