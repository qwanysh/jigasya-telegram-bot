from telegram.ext import Filters, MessageHandler

from src import config


def render_message(template_name, *args, **kwargs):
    template = config.jinja2_env.get_template(template_name)
    return template.render(*args, **kwargs)


def get_middleware_handler(handler):
    return MessageHandler(Filters.all, handler)
