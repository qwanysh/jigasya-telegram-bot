from telegram import Update
from telegram.ext import CallbackContext


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text('I\'m here!')


def chat_info_handler(update: Update, context: CallbackContext):
    update.message.reply_text(update.to_json())
