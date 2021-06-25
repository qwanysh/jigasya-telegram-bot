from src import bot, config

WEBBOOK_URL_TEMPLATE = 'https://{}.herokuapp.com/{}'


def main():
    if config.HEROKU_APP_NAME:
        bot.start_webhook(
            listen='0.0.0.0',
            port=int(config.PORT),
            url_path=config.TOKEN,
            webhook_url=WEBBOOK_URL_TEMPLATE.format(
                config.HEROKU_APP_NAME, config.TOKEN,
            ),
        )
        bot.idle()
    else:
        bot.start_polling()


if __name__ == '__main__':
    main()
