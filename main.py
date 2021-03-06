from telegram.ext import * 
from telegram import *

import os
import multiprocessing

from flask import Flask
from threading import Thread

import json

from BotModules import FlaskKeepAlive as FlaskKeepAlive

from BotModules import YtsSearcher as YtsSearcher
from BotModules import bothelp as bothelp
from BotModules import o1337xSearcher as o1337xSearcher
from BotModules import NyaasiSearcher as NyaasiSearcher

# Reading the config.txt file to get configuration details
with open('config.json') as json_file:
    print('[+] Reading config Data')
    ConfigData = json.load(json_file)
print('[√] Config Data read successfully')

def yts_command(update, context):
    RecievedMsg = update.message.text
    CommandToReplace = ConfigData['COMMANDS']['Yts']


    YtsSearcher.YTSsearch(update, context, RecievedMsg, CommandToReplace)


def BotHelp(update, context):
    HelpMessage = bothelp.BotHelpMessage(ConfigData['COMMANDS'])

    ChatID = update.message.chat_id
    context.bot.sendMessage(chat_id = ChatID, text = HelpMessage, parse_mode = ParseMode.HTML)
    
def o1337x(update, context):

    RecievedMsg = update.message.text                       # Getting the message sent by the user
    MessageID = update.message.message_id                   # Required to reply to that message

    CommandToReplace = ConfigData['COMMANDS']['o1337x']     # Getting the command, alloted 10 1337x search
    NoOf1337xResults = int(ConfigData['NoOf1337xResults'])  # Getting the number of torrents to be fetched

    o1337xSearcher.Get1337x(RecievedMsg, CommandToReplace, NoOf1337xResults, MessageID, update, context)

def Nyaasi_Command(update, context):

    RecievedMsg = update.message.text
    MessageID = update.message.message_id

    CommandToReplace = ConfigData['COMMANDS']['Nyaasi']
    NoNyaasiResults = int(ConfigData['NoNyaasiResults'])

    NyaasiSearcher.NYAASIsearch(RecievedMsg, CommandToReplace, NoNyaasiResults, MessageID, update, context)


def BotMain(seconds):
    if (ConfigData['Deploy'] == '1'):
        my_secret = os.environ['API_KEY']
    else:
        my_secret = ConfigData['API_KEY']
    updater = Updater(my_secret, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler(f"{ConfigData['COMMANDS']['Yts']}", yts_command))
    dp.add_handler(CommandHandler(f"{ConfigData['COMMANDS']['Help']}", BotHelp))
    dp.add_handler(CommandHandler(f"{ConfigData['COMMANDS']['o1337x']}", o1337x))
    dp.add_handler(CommandHandler(f"{ConfigData['COMMANDS']['Nyaasi']}", Nyaasi_Command))

    updater.start_polling()
    print("\n[√] BOT STARTED SUCCESSFULLY [√]\n")
    updater.idle()

# Running multithreads

p1 = multiprocessing.Process(target=BotMain, args=[1])
p2 = multiprocessing.Process(target=FlaskKeepAlive.FlaskApp, args=[1])

if __name__ == '__main__':
    p1.start()
    p2.start()
    
    
