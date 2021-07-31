from datetime import datetime

from telegram import (ForceReply, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                      Update)
from telegram.ext import (CallbackContext, CommandHandler, ConversationHandler,
                          Filters, MessageHandler)

from src import database, models
from src.utils import permissions

UPDATE, BIRTH_DATE = range(2)


@permissions.jigasya_chat_only
def entry_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    with database.Session() as session:
        member = session.query(models.JigasyaMember).get(from_user.id)
        if member:
            reply_markup = ReplyKeyboardMarkup(
                [['Да']], one_time_keyboard=True, resize_keyboard=True,
                selective=True,
            )
            update.message.reply_text(
                f'{member} уже зарегистрирован. Обновить информацию? /cancel '
                f'для отмены', reply_markup=reply_markup,
            )
            return UPDATE
        else:
            member = models.JigasyaMember(
                telegram_id=from_user.id, username=from_user.username,
                first_name=from_user.first_name, last_name=from_user.last_name,
            )
            session.add(member)
            session.commit()
            reply_markup = ForceReply(
                selective=True, input_field_placeholder='dd.mm.yyyy',
            )
            update.message.reply_html(
                f'{member} успешно зарегистрирован. Введите дату рождения в '
                f'формате <code>dd.mm.yyyy</code>. /cancel для отмены',
                reply_markup=reply_markup,
            )
            return BIRTH_DATE


def update_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    with database.Session() as session:
        member = session.query(models.JigasyaMember).get(from_user.id)
        member.username = from_user.username
        member.first_name = from_user.first_name
        member.last_name = from_user.last_name
        session.commit()
        reply_markup = ForceReply(
            selective=True, input_field_placeholder='dd.mm.yyyy',
        )
        update.message.reply_html(
            f'{member} успешно обновлен. Введите дату рождения в формате '
            f'<code>dd.mm.yyyy</code>. /cancel для отмены',
            reply_markup=reply_markup,
        )
    return BIRTH_DATE


def birth_date_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    try:
        birth_date = datetime.strptime(update.message.text, '%d.%m.%Y').date()
        with database.Session() as session:
            member = session.query(models.JigasyaMember).get(from_user.id)
            member.birth_date = birth_date
            session.commit()
            update.message.reply_text(
                f'Дата рождения {member} сохранена',
                reply_markup=ReplyKeyboardRemove(),
            )
        return ConversationHandler.END
    except ValueError:
        reply_markup = ForceReply(
            selective=True, input_field_placeholder='dd.mm.yyyy',
        )
        update.message.reply_html(
            'Указанная дата некорректна. Попробуйте еще раз. /cancel для '
            'отмены', reply_markup=reply_markup,
        )
        return BIRTH_DATE


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
        BIRTH_DATE: [
            MessageHandler(
                Filters.regex(r'^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$'),
                birth_date_handler,
            ),
            CommandHandler('cancel', cancel_handler),
        ],
    },
    fallbacks=[],
)
