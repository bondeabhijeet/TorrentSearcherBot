import requests 

def GetTorrentDetails(AllTorrents, QueryQuality):
    for quality in AllTorrents:
        if(quality['quality'] == QueryQuality):
            return(quality)

    return 0
         
def YTSsearch(RecievedMsg, CommandToReplace):

    BaseURL = "https://yts.mx/api/v2/list_movies.json"
    ValidQualities = ["720p", "1080p", "2160p", "3D"]

    results = str()

    query = RecievedMsg.replace(f'/{CommandToReplace} ', '').replace(f'/{CommandToReplace}', '')

    FilteredList = query.split("|")
    QueryName = FilteredList[0].strip()

    if(QueryName == '' or QueryName in ValidQualities):
        return("<b>[✗] : ᴘʟᴇᴀꜱᴇ ꜱᴘᴇᴄɪꜰʏ ꜱᴇᴀʀᴄʜ ᴛᴇʀᴍ</b>")

    try:
        QueryQuality = FilteredList[1].strip()

        if QueryQuality in ValidQualities:
            results = f"Qᴜᴀʟɪᴛʏ ꜱᴇʟᴇᴄᴛᴇᴅ : <code>{QueryQuality}</code>\n"
        else:
            return "[✗] 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 "
    except:
        QueryQuality = "1080p"
        results = "Qᴜᴀʟɪᴛʏ ꜱᴇʟᴇᴄᴛᴇᴅ : <code>1080ᴘ (ᴅᴇꜰᴀᴜʟᴛ)</code>\n"

    payload={'query_term':QueryName, 'quality':QueryQuality}
    response = requests.get(BaseURL, params=payload)

    if(response.ok):
        print(f"[🔍] Searching for {QueryName} in {QueryQuality}")
        MoviesRecieved = response.json()['data']
        NumberOfMovies = MoviesRecieved['movie_count']
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
                msg = "Invalid Quality Specified"
                return(msg)

            results = results + f"𝙉𝙖𝙢𝙚: <code><b>{Name}</b></code> \n𝙔𝙚𝙖𝙧: <code>{Year}</code> \n𝙈𝙤𝙫𝙞𝙚 𝙌𝙪𝙖𝙡𝙞𝙩𝙮: <code>{MovieQuality}</code> \n𝙈𝙤𝙫𝙞𝙚 𝙎𝙞𝙯𝙚: <code>{MovieSize}</code> \n𝙏𝙤𝙧𝙧𝙚𝙣𝙩 𝙇𝙞𝙣𝙠: <code>{TorrentDownloadLink}</code>" + "\n\n"
        
        return results
    else:
        return "<b>[Opps...] Something went wrong </b>"
