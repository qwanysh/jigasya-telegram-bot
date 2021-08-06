from sqlalchemy import func
from telegram import Update
from telegram.ext import CallbackContext

from src import database, models
from src.utils import helpers, permissions


@permissions.jigasya_chat_only
def find_dolbaeb_handler(update: Update, context: CallbackContext):
    with database.Session() as session:
        random_member = session.query(
            models.JigasyaMember,
        ).order_by(func.random()).first()
    message = helpers.render_message('find_dolbaeb.html', member=random_member)
    update.message.reply_html(message)
