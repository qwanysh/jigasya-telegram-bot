from telegram import Update
from telegram.ext import CallbackContext

from src import database, models
from src.utils import helpers, permissions


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text('Я тут!')


@permissions.superuser_only
def chat_info_handler(update: Update, context: CallbackContext):
    update.message.reply_text(update.to_json())


@permissions.jigasya_chat_only
def members_handler(update: Update, context: CallbackContext):
    with database.Session() as session:
        members = session.query(models.JigasyaMember).order_by(
            models.JigasyaMember.created_at.desc(),
        )
    message = helpers.render_message('members.html', members=members)
    update.message.reply_html(message, disable_notification=True)
