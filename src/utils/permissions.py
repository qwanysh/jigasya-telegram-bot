from functools import wraps

from telegram import Update
from telegram.ext import CallbackContext

from src import config


def superuser_only(func):
    @wraps(func)
    def wrapper(update: Update, context: CallbackContext):
        if update.message.from_user.id == config.SUPERUSER_ID:
            return func(update, context)

    return wrapper


def jigasya_chat_only(func):
    @wraps(func)
    def wrapper(update: Update, context: CallbackContext):
        if update.message.chat.id == config.JIGASYA_CHAT_ID:
            return func(update, context)

    return wrapper
