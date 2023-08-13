from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater
from scrape import *

TOKEN = 'token'
bot_usname = '@Filmother_bot'
# find information about the movie +++
# find information about the actor +++
# find information about tops +++


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I`m Filmother. I know everything(or almost everything🙂) about movies🎥. '
                                    'So, I`m ready to help you😇.\nHere all my commands:\n/help --> all commands\n'
                                    '/film_list --> list of movies by genre\n/actor --> information about the actor\n'
                                    '/movie --> information about the movie')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'There is error {context.error} from {update}')



async def tops(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Write one of movie genre in the format:"Genre: {your genre}" \n(if you need only ukrainian movies, write "ua" after genre, example:"Genre: travel, ua"):\n🎞Comedy🎭\n🎞Entertaining😁\n🎞Action🔫\n🎞Detective🕵️‍♀\n🎞Melodrama❤️\n🎞Thriller😬\n🎞Horror🙀\n🎞Musical🎵\n🎞Western🤠\n🎞Adventures😎\n🎞Sport🤾‍♀️\n🎞Sci-Fi👽\n🎞Crime👮‍♀️\n🎞Drama❤️\n🎞Short🎬\n🎞History🤴\n🎞Documentary🌟\n🎞Family👨‍👩‍👧‍👦\n🎞Cooking🍪\n🎞Travel🌴\n🎞Kids👶\n🎞Comics🦸‍♀️\n🎞Fantasy🧚‍♂️\n🎞All🎥')


async def find_information_about_actor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Write name and surname of an actor in the format:"Actor/Actress: {name surname}"')


async def find_information_about_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Write movie title in the format:"Movie: {title}"')


def responses(text):
    text = text.lower()
    if 'hello' in text:
        return 'Hi!👋'
    elif text.startswith('genre') and len(text[text.index(':')+1:].strip())!=0:
        text_elems = text[6:].split(',')
        ua = False
        if text_elems[0].strip() in \
                ['comedy', 'entertaining', 'action', 'detective', 'melodrama', 'thriller', 'horror', 'musical', 'western', 'adventures', 'sport', 'sci-fi', 'crime', 'drama', 'sport', 'history', 'documentary', 'family', 'cooking', 'travel', 'kids', 'comics', 'fantasy', 'all']:
            genre = text_elems[0].strip()
            if genre == 'sci-fi':
                genre = 'fiction'
            elif genre == 'all':
                genre = None
        if text.endswith('ua'):
            ua = True
        return 'Films:\n🌟'+'\n\n🌟'.join(find_top(video_genre_id=genre, ua=ua))
    elif text.startswith('actor') and len(text[text.index(':')+1:].strip())!=0:
        actor = text[text.index(':')+1:].strip()
        return 'Actor:\n'+'\n'.join(find_(name=actor))
    elif text.startswith('movie') and len(text[text.index(':')+1:].strip())!=0:
        movie = text[text.index(':')+1:].strip()
        return 'Movie:\n'+'\n'.join(find_(name=movie, actor=False))
    return 'There is a mistake in the message'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    txt = update.message.text
    print(f'User {update.message.chat.id} in {message_type}: "{txt}')
    if message_type == 'group':
        if bot_usname in txt:
            new_text = txt.replace(bot_usname, '').strip()
            response = responses(new_text)
        else:
            return
    else:
        response = responses(txt)
    print('Bot:', response)
    await update.message.reply_text(response)
