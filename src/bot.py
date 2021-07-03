from datetime import time

from telegram.ext import CommandHandler, Updater

from src import config, handlers

bot = Updater(token=config.TOKEN)

dispatcher = bot.dispatcher
dispatcher.add_handler(CommandHandler('start', handlers.start_handler))
dispatcher.add_handler(CommandHandler('chat_info', handlers.chat_info_handler))
dispatcher.add_handler(
    CommandHandler('register', handlers.register_member_handler),
)
dispatcher.add_handler(
    CommandHandler('find_dolbaeb', handlers.find_dolbaeb_handler),
)

job_queue = bot.job_queue
job_queue.run_daily(
    handlers.bugin_ne_plan_handler, time=time(hour=12), days=[4],
)
