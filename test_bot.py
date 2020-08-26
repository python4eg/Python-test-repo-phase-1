import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger('BOT')

def echo(update, context):
    update.message.reply_text(update.message.text)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://rozetka.com.ua/151663121/p151663121/")

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

if __name__ == '__main__':
    updater = Updater(token='TOlKiEN', use_context=True)
    start_handler = CommandHandler('start', start)
    caps_handler = CommandHandler('caps', caps)
    updater.dispatcher.add_handler(caps_handler)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()