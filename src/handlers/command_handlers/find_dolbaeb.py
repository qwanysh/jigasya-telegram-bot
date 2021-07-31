from sqlalchemy import func
from telegram import Update
from telegram.ext import CallbackContext

from src import database, models
from src.utils import permissions


@permissions.jigasya_chat_only
def find_dolbaeb_handler(update: Update, context: CallbackContext):
    with database.Session() as session:
        random_member = session.query(
            models.JigasyaMember,
        ).order_by(func.random()).first()
    if random_member:
        text = f'Долбаёб найден: {random_member}'
    else:
        text = 'Долбаёб не найден'
    update.message.reply_text(text)
