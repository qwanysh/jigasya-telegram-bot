from sqlalchemy.exc import IntegrityError
from telegram import Update
from telegram.ext import CallbackContext

from src import models, database
from src.utils import permissions


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text('I\'m here!')


@permissions.superuser_only
def chat_info_handler(update: Update, context: CallbackContext):
    update.message.reply_text(update.to_json())


@permissions.jigasya_chat_only
def register_member_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    member = models.JigasyaMember(
        telegram_id=from_user.id, username=from_user.username,
        first_name=from_user.first_name, last_name=from_user.last_name,
    )
    session = database.SessionLocal()
    session.add(member)
    try:
        session.commit()
        text = f'Member @{from_user.username} registered successfully'
    except IntegrityError:
        text = f'Member @{from_user.username} is already registered'
    session.close()
    update.message.reply_text(text)
