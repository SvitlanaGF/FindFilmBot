from telegram_bot import *

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler("film_list", tops))
    app.add_handler(CommandHandler('actor', find_information_about_actor))
    app.add_handler(CommandHandler('movie', find_information_about_movie))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    app.run_polling(poll_interval=3)

