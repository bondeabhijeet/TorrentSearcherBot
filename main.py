from telegram.ext import * 
from telegram import *

import json

from BotModules import TorrentSearcher as TorrentSearcher
from BotModules import bothelp as bothelp

# Reading the config.txt file to get configuration details
with open('config.json') as json_file:
    print('[+] Reading config Data')
    ConfigData = json.load(json_file)
print('[√] Config Data read successfully')

def yts_command(update, context):
    RecievedMsg = update.message.text
    #query = RecievedMsg.replace("/yts ", '')

    ChatID = update.message.chat_id
    print("Chat ID:", ChatID)

    msg = context.bot.sendMessage(chat_id = ChatID, text = "<b>Searching...</b>", parse_mode = ParseMode.HTML)

    results = TorrentSearcher.YTSsearch(RecievedMsg, ConfigData['COMMANDS']['Yts'])

    msg.edit_text(results, parse_mode=ParseMode.HTML)

def BotHelp(update, context):
    HelpMessage = bothelp.BotHelpMessage(ConfigData['COMMANDS'])

    ChatID = update.message.chat_id
    context.bot.sendMessage(chat_id = ChatID, text = HelpMessage, parse_mode = ParseMode.HTML)
    

def main():
    updater = Updater(ConfigData['API_KEY'], use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler(f"{ConfigData['COMMANDS']['Yts']}", yts_command))
    dp.add_handler(CommandHandler(f"{ConfigData['COMMANDS']['Help']}", BotHelp))

    updater.start_polling()
    updater.idle()

main()