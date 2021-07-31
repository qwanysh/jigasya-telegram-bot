from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (CallbackContext, CommandHandler, ConversationHandler,
                          Filters, MessageHandler)

from src import database, models
from src.utils import permissions

UPDATE = range(1)


@permissions.jigasya_chat_only
def entry_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    with database.Session() as session:
        member = session.query(models.JigasyaMember).get(from_user.id)
        if member:
            reply_markup = ReplyKeyboardMarkup(
                [['Да', '/cancel']], one_time_keyboard=True,
                resize_keyboard=True, selective=True,
            )
            update.message.reply_text(
                f'{member} уже зарегистрирован. Обновить информацию?',
                reply_markup=reply_markup,
            )
            return UPDATE
        else:
            member = models.JigasyaMember(
                telegram_id=from_user.id, username=from_user.username,
                first_name=from_user.first_name, last_name=from_user.last_name,
            )
            session.add(member)
            session.commit()
            update.message.reply_text(f'{member} успешно зарегистрирован')
            return ConversationHandler.END


def update_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    with database.Session() as session:
        member = session.query(models.JigasyaMember).get(from_user.id)
        member.username = from_user.username
        member.first_name = from_user.first_name
        member.last_name = from_user.last_name
        session.commit()
        update.message.reply_text(
            f'{member} успешно обновлен', reply_markup=ReplyKeyboardRemove(),
        )
    return ConversationHandler.END


def cancel_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Действие отменено', reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


register_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('register', entry_handler)],
    states={
        UPDATE: [
            MessageHandler(Filters.regex('^Да$'), update_handler),
            CommandHandler('cancel', cancel_handler),
        ],
    },
    fallbacks=[],
)
