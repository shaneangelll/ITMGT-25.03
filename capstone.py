import constants as keys
from telegram.ext import *
import responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text("𝐆𝐨𝐨𝐝 𝐝𝐚𝐲, 𝐯𝐚𝐥𝐮𝐞𝐝 𝐆𝐮𝐞𝐬𝐭! (´｡• ᵕ •｡`) ♡\n\nThank you for choosing to dine with us here at our hotel. Send any of the following texts below for better assistance. \n\n ❥ 𝐖𝐡𝐨 𝐚𝐫𝐞 𝐲𝐨𝐮? | Provides details about this bot \n ❥ 𝐌𝐞𝐚𝐥 𝐓𝐢𝐦𝐞𝐬 | Sends the list of meal times for your reference \n ❥ 𝐎𝐫𝐝𝐞𝐫 𝐍𝐨𝐰 | Sends the menu if it is time for a meal")

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
