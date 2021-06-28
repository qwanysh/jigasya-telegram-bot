from telegram.ext import Updater, CommandHandler

from src import config, handlers

bot = Updater(token=config.TOKEN)

dispatcher = bot.dispatcher
dispatcher.add_handler(CommandHandler('start', handlers.start_handler))
dispatcher.add_handler(CommandHandler('chat_info', handlers.chat_info_handler))
