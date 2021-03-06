import constants as keys
from telegram.ext import *
import responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text("๐๐จ๐จ๐ ๐๐๐ฒ, ๐ฏ๐๐ฅ๐ฎ๐๐ ๐๐ฎ๐๐ฌ๐ญ! (ยด๏ฝกโข แต โข๏ฝก`) โก\n\nThank you for choosing to dine with us here at our hotel. Send any of the following texts below for better assistance. \n\n โฅ ๐๐ก๐จ ๐๐ซ๐ ๐ฒ๐จ๐ฎ? | Provides details about this bot \n โฅ ๐๐๐๐ฅ ๐๐ข๐ฆ๐๐ฌ | Sends the list of meal times for your reference \n โฅ ๐๐ซ๐๐๐ซ ๐๐จ๐ฐ | Sends the menu if it is time for a meal")

def help_command(update, context):
    update.message.reply_text("What can I help you with?")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
  # wtf is updater
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling(3)
    updater.idle()

main()
