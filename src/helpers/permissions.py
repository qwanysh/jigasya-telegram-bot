from functools import wraps

from telegram import Update
from telegram.ext import CallbackContext

from src import config


def superuser_only(func):
    @wraps(func)
    def wrapper(update: Update, context: CallbackContext):
        if update.message.from_user.id == int(config.SUPERUSER_ID):
            func(update, context)

    return wrapper
