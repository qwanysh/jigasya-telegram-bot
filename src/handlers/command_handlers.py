from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import func
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, ConversationHandler, CommandHandler, \
    MessageHandler, Filters

from src import database, models
from src.utils import permissions


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text('I\'m here!')


@permissions.superuser_only
def chat_info_handler(update: Update, context: CallbackContext):
    update.message.reply_text(update.to_json())


def register_member_entry_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    with database.Session() as session:
        member = session.query(models.JigasyaMember).get(from_user.id)
        if not member:
            member = models.JigasyaMember(
                telegram_id=from_user.id, username=from_user.username,
                first_name=from_user.first_name, last_name=from_user.last_name,
            )
            session.add(member)
            session.commit()
            update.message.reply_text(f'{member} успешно зарегистрирован')
            return ConversationHandler.END
        else:
            update.message.reply_text(f'{member} уже зарегистрирован. Обновить информацию(/update)?')
            return 1


def register_member_update_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    with database.Session() as session:
        member = session.query(models.JigasyaMember).get(from_user.id)
        member.username = from_user.username
        member.first_name = from_user.first_name
        member.last_name = from_user.last_name
        session.commit()
        update.message.reply_text(f'{member} успешно обновлен')
    return ConversationHandler.END


def cancel_handler(update: Update, context: CallbackContext):
    update.message.reply_text('Операция отменена')
    return ConversationHandler.END


register_member_handler = ConversationHandler(
    entry_points=[CommandHandler('register', register_member_entry_handler)],
    states={
        1: [CommandHandler('update', register_member_update_handler)],
    },
    fallbacks=[MessageHandler(Filters.all, cancel_handler)],
)



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
