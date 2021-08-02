from telegram import Update
from telegram.ext import CallbackContext

from src.utils import permissions


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text('Я тут!')


@permissions.superuser_only
def chat_info_handler(update: Update, context: CallbackContext):
    update.message.reply_text(update.to_json())