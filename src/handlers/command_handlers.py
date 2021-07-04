from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import func
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from src import database, models
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
    with database.Session() as session:
        session.add(member)
        try:
            session.commit()
            text = f'Member `#{member.telegram_id}` registered successfully'
        except IntegrityError:
            text = f'Member `#{member.telegram_id}` is already registered'
    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN_V2)


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
