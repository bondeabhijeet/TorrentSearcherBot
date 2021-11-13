import requests
import telegram
from telegram.parsemode import ParseMode
from BotModules import SendMessage as SendMessage

def GetTorrentDetails(AllTorrents, QueryQuality):
    for quality in AllTorrents:
        if(quality['quality'] == QueryQuality):
            return(quality)
    return 0

def ValidQuery(RecievedMsg, CommandToReplace, context):
    
    CommandWithBotname = CommandToReplace + context.bot.bot.name
    query = RecievedMsg.replace(f'/{CommandWithBotname}', '').replace(f'/{CommandToReplace}', '')
    query = query.strip()

    if(query == ''):
        return None
    else:
        return query


def EditMessage(msg, TextToUpdate):
    msg.edit_text(TextToUpdate, parse_mode=ParseMode.HTML)

def YTSsearch(update, context, RecievedMsg, CommandToReplace):
    MessageID = update.message.message_id

    msg = SendMessage.SendMessage(update, context, "<b>Searching...</b>", MessageID)

    BaseURL = "https://yts.mx/api/v2/list_movies.json"
    ValidQualities = ["720p", "1080p", "2160p", "3D"]

    results = str()

    query = ValidQuery(RecievedMsg, CommandToReplace, context)   # Extract (the valid) query from the command
    if(query == None):                                  # Check if the user has sent a query or is it just the command
        EditMessage(msg, "<b>[✗] : ᴘʟᴇᴀꜱᴇ ꜱᴘᴇᴄɪꜰʏ ꜱᴇᴀʀᴄʜ ᴛᴇʀᴍ</b>")
        return

    FilteredList = query.split("|")
    QueryName = FilteredList[0].strip()

    if(QueryName in ValidQualities):
        EditMessage(msg, "<b>[✗] : ᴘʟᴇᴀꜱᴇ ꜱᴘᴇᴄɪꜰʏ ꜱᴇᴀʀᴄʜ ᴛᴇʀᴍ</b>")
        return

    try:
        QueryQuality = FilteredList[1].strip()

        if QueryQuality in ValidQualities:
            results = f"Qᴜᴀʟɪᴛʏ ꜱᴇʟᴇᴄᴛᴇᴅ : <code>{QueryQuality}</code>\n"
        else:
            EditMessage(msg, "<b>[✗] 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 </b>")
            return
    except:
        QueryQuality = "1080p"
        results = "Qᴜᴀʟɪᴛʏ ꜱᴇʟᴇᴄᴛᴇᴅ : <code>1080ᴘ (ᴅᴇꜰᴀᴜʟᴛ)</code>\n"

    payload={'query_term':QueryName, 'quality':QueryQuality}
    response = requests.get(BaseURL, params=payload)

    if(response.ok):
        print(f"[🔍] Searching for {QueryName} in {QueryQuality}")
        MoviesRecieved = response.json()['data']
        NumberOfMovies = MoviesRecieved['movie_count']
        if (NumberOfMovies == 0):
            EditMessage(msg, "<b>No results for the search query.</b>")
            return
        else:
            None
            
        MovieNames = MoviesRecieved['movies']

        results = results + f"ɴᴜᴍʙᴇʀ ᴏғ ᴍᴏᴠɪᴇs ғᴇᴛᴄʜᴇᴅ: <code>{NumberOfMovies}</code>\n\n"

        for Movie in MovieNames:
            AllTorrents = Movie['torrents']
            
            Name = Movie['title']
            Year = Movie['year']            
            
            SelectedDetails = GetTorrentDetails(AllTorrents, QueryQuality)
            if (SelectedDetails):
                MovieQuality = SelectedDetails['quality']
                MovieSize = SelectedDetails['size']
                TorrentDownloadLink = SelectedDetails['url']
            else:
                SendMessage.SendMessage(update, context, "<b>[✗] No results for the specified search query.</b>", MessageID)
                return

            results = results + f"𝙉𝙖𝙢𝙚: <code><b>{Name}</b></code> \n𝙔𝙚𝙖𝙧: <code>{Year}</code> \n𝙈𝙤𝙫𝙞𝙚 𝙌𝙪𝙖𝙡𝙞𝙩𝙮: <code>{MovieQuality}</code> \n𝙈𝙤𝙫𝙞𝙚 𝙎𝙞𝙯𝙚: <code>{MovieSize}</code> \n𝙏𝙤𝙧𝙧𝙚𝙣𝙩 𝙇𝙞𝙣𝙠: <code>{TorrentDownloadLink}</code>" + "\n\n"
        
        EditMessage(msg, results)
    else:
        SendMessage.SendMessage(update, context, "<b>[✗] [Opps...] Something went wrong [✗]</b>", MessageID)
        return