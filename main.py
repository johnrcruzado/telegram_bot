import os

import Constants as keys
from telegram.ext import *
import bot_reponse as R
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

print("Bot started...")
updater = Updater(keys.API_KEY)
dp = updater.dispatcher


def start_command(update , context):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='hi'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    #update.message.reply_text('Please choose:', reply_markup=reply_markup,)
    #update.message.edit_media(media=InputMediaPhoto(media=open('http://kolabph.com/media/documents/isaw_1_4uqLgI2.jpg', 'rb'), caption='Title'))

    update.message.reply_text('Please choose:', reply_markup=reply_markup)




def help_command(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    #update.message.reply_text("If you need help you should ask for it on Google!")
    filename = r"C:\Users\admin\Desktop\working_Project\telegram bot\image.png"
    #update.message.bot.send_photo(update.message.chat.id,open(filename,'rb'), caption='Title', reply_markup=reply_markup)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def buy_command(update, context):
    keyboard = [ [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    #update.message.reply_text("If you need help you should ask for it on Google!")

    filename = r"C:\Users\admin\Desktop\working_Project\telegram bot\image.png"
    context.bot.send_photo(update.message.chat.id,open(filename,'rb'), caption='Title', reply_markup=reply_markup)

    #update.message.reply_text('Please choose:', reply_markup=reply_markup)



def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)


def handle_photo(update, context):
    text = str(update.message.text).lower()
    update.message.edit_media(media=InputMediaPhoto(media=open('http://kolabph.com/media/documents/isaw_1_4uqLgI2.jpg', 'rb'), caption='Title'))


def error(update,context):
    print(f"Update {update} caused error{context.error}")



def button(update: Update, _: CallbackContext) -> None:
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    print(query.data)

    #query.edit_message_media(text=f"Selected option: {query.data}")
    query.bot.sendMessage(chat_id=query.message.chat_id,text="Thank you")


def main():

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("buy", buy_command))
    dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    #dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
