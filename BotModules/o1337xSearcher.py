from py1337x import py1337x
from telegram.parsemode import ParseMode
import os
import time

################################### Function to get the magnet link for specific torrent

def GetMagnet(Link, torrents):
    TorrentInfo = torrents.info(link=Link)
    return TorrentInfo['magnetLink']

################################### Function to Create a message to be sent to the user as response

def CreateMessage(Name, Size, Seeders, Leechers, UploadedAt, MagnetLink):
    MsgToSend = f"""Name: <code><b>{Name}</b></code> 
Size: <code>{Size}</code> 
Seeders: <code>{Seeders}</code> 
Leechers: <code>{Leechers}</code> 
Uploaded at: <code>{UploadedAt}</code> 
Magnet: <code>{MagnetLink}</code>"""

    return MsgToSend

################################### Function to sent the message to the user that was created earlier

def SendMessage(update, context, MsgText, MessageID):
    Chat_ID = update.message.chat_id

    msg = context.bot.sendMessage(chat_id = Chat_ID, text = MsgText, reply_to_message_id=MessageID, parse_mode = ParseMode.HTML)
    time.sleep(0.8)
    return

################################### Extract (the valid) query from the provided command by the user

def ValidQuery(RecievedMsg, CommandToReplace, context):
    
    CommandWithBotname = CommandToReplace + context.bot.bot.name
    query = RecievedMsg.replace(f'/{CommandWithBotname}', '').replace(f'/{CommandToReplace}', '')
    query = query.strip()

    if(query == ''):
        return None
    else:
        return query

################################### MAIN 

def Get1337x(RecievedMsg, CommandToReplace, NoOf1337xResults, MessageID, update, context):

    query = ValidQuery(RecievedMsg, CommandToReplace, context)   # Extract (the valid) query from the command

    if(query == None):                                  # Check if the user has sent a query or is it just the command
        SendMessage(update, context, "Enter a search term", MessageID)
        return
    else:
        print(f"[🔍] Searching for {query}")

    CurrentDirectoryPath = os.getcwd()                  # Get the full path to working directory (to save cache for py1337x library)
    try:
        torrents = py1337x(proxy='1337x.wtf', cache= CurrentDirectoryPath, cacheTime=500)
    except:
        torrents = py1337x(proxy='1337xx.to', cache= CurrentDirectoryPath, cacheTime=500)

    RawJsonData = torrents.search(f'{query}')           # Using the py1337x library to get the search results for query provided

    if(RawJsonData['itemCount'] == 0):                  # If there are 0 results for the query
        SendMessage(update, context, "NO RESULTS FOR THE REQUESTED QUERY", MessageID)
        return
    else:
        None

    for i in range(0, NoOf1337xResults):                # Getting information for each torrent
        Torrent = RawJsonData['items'][i]

        Name = Torrent['name']                              # NAME OF THE TORRENT
        Size = Torrent['size']                              # SIZE OF THE TORRENT
        Seeders = Torrent['seeders']                        # SEEDERS OF THE TORRENT
        Leechers = Torrent['leechers']                      # LEECHERS OF THE TORRENT
        UploadedAt = Torrent['time']                        # TIME OF UPLOAD OF THE TORRENT
        MagnetLink = GetMagnet(Torrent['link'], torrents)   # GET THE MAGNET LINK FOR THE TORRENT

        MsgToSend = CreateMessage(Name, Size, Seeders, Leechers, UploadedAt, MagnetLink)    # Creating the message to send (contains details of only 1 torrent)

        SendMessage(update, context, MsgToSend, MessageID)

    return
