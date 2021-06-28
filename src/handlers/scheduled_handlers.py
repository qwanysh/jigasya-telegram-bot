from telegram.ext import CallbackContext

from src import config


def bugin_ne_plan_handler(context: CallbackContext):
    context.bot.send_message(
        chat_id=config.JIGASYA_CHAT_ID, text='Бүгін не план?',
    )
