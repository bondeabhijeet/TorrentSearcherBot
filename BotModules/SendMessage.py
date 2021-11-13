from telegram.parsemode import ParseMode
import time

def SendMessage(update, context, MsgText, MessageID):
    Chat_ID = update.message.chat_id

    msg = context.bot.sendMessage(chat_id = Chat_ID, text = MsgText, reply_to_message_id=MessageID, parse_mode = ParseMode.HTML)
    time.sleep(0.8)
    return msg