import requests
from bs4 import BeautifulSoup
from telegram.parsemode import ParseMode

def WhoIsLess(NoNyaasiResults, NumberOfTrs):
  if(NoNyaasiResults <= NumberOfTrs):
    return NoNyaasiResults
  else:
    return NumberOfTrs

def ValidQuery(RecievedMsg, CommandToReplace):
    query = RecievedMsg.replace(f'/{CommandToReplace} ', '').replace(f'/{CommandToReplace}', '').replace(f'/{CommandToReplace.lower()}', '').replace(f'/{CommandToReplace.lower()} ', '')
    if(query == ''):
        return None
    else:
        return query

def SendMessage(update, context, MsgText, MessageID):
    Chat_ID = update.message.chat_id

    msg = context.bot.sendMessage(chat_id = Chat_ID, text = MsgText, reply_to_message_id=MessageID, parse_mode = ParseMode.HTML)
    return

def CreateMessage(Name, Size, Seeders, Leechers, DownloadCompleted, MagnetLink):
    MsgToSend = f"""Name: <code><b>{Name}</b></code> 
Size: <code>{Size}</code> 
Seeders: <code>{Seeders}</code> 
Leechers: <code>{Leechers}</code> 
Completed Downloads: <code>{DownloadCompleted}</code> 
Magnet: <code>{MagnetLink}</code>"""

    return MsgToSend

def NYAASIsearch(RecievedMsg, CommandToReplace, NoNyaasiResults, MessageID, update, context):

    query = ValidQuery(RecievedMsg, CommandToReplace)   # Extract (the valid) query from the command

    if(query == None):                                  # Check if the user has sent a query or is it just the command
        SendMessage(update, context, "Enter a search term", MessageID)
        return
    else:
        print(f"[🔍] Searching for {query}")
    
    payload = {
        'q' : query
    }
    
    r = requests.get('https://nyaa.si/', params=payload).text

    soup = BeautifulSoup(r, 'lxml')

    tbody = soup.find('tbody')
    try:
      trs = tbody.find_all('tr')
    except:
      SendMessage(update, context, "NO RESULTS FOR THE REQUESTED QUERY", MessageID)
      return

    MaxLimit = WhoIsLess(NoNyaasiResults, len(trs))

    for i in range(0, MaxLimit):
        tr = trs[i]
        tds = tr.find_all('td')

        Name = tds[1].find_all('a')[-1].text
        Size = tds[-5].text
        MagnetLink = tds[-6].find_all('a')[-1]['href']
        DownloadCompleted = tds[-1].text
        Leechers = tds[-2].text
        Seeders = tds[-3].text

        MsgToSend = CreateMessage(Name, Size, Seeders, Leechers, DownloadCompleted, MagnetLink)    # Creating the message to send (contains details of only 1 torrent)

        SendMessage(update, context, MsgToSend, MessageID)
        

    return
