from telegram import Update
from telegram.ext import CallbackContext

from src import consts, database, models
from src.redis_client import redis_client
from src.utils import permissions


@permissions.jigasya_chat_only
def register_handler(update: Update, context: CallbackContext):
    from_user = update.message.from_user
    redis_key = f'registered_member:{from_user.id}'

    if redis_client.get(redis_key):
        return

    with database.Session() as session:
        member = session.query(models.JigasyaMember).get(from_user.id)

    if member:
        member.username = from_user.username
        member.first_name = from_user.first_name
        member.last_name = from_user.last_name

        with database.Session() as session, session.begin():
            session.add(member)
    else:
        member = models.JigasyaMember(
            telegram_id=from_user.id, username=from_user.username,
            first_name=from_user.first_name, last_name=from_user.last_name,
        )
        with database.Session() as session, session.begin():
            session.add(member)

    redis_client.setex(redis_key, consts.REGISTER_CACHE_TTL, from_user.id)
