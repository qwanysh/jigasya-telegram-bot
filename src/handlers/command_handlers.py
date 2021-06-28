from telegram import Update
from telegram.ext import CallbackContext

from src.helpers import permissions


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text('I\'m here!')


@permissions.superuser_only
def chat_info_handler(update: Update, context: CallbackContext):
    update.message.reply_text(update.to_json())
