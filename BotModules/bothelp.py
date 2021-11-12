


def BotHelpMessage(Commands):
    print(Commands)

    Msg = f"""
/{Commands['Help']}
>> Will get this message.

/{Commands['Yts']} <code>[ movie name ]</code> | <code>[ quality of the movie ]</code>
<b>NOTE: by default quality is 1080p.</b>
>> Will get the Direct Download Links of torrents avaliable for the specified movie name with mentioned quality

/{Commands['o1337x']} <code>[ Search query ]</code>
>> Will get the Torrent details and their magnet link avaliable for the specified Search query.

/{Commands['Nyaasi']} <code>[ Search query ]</code>
<b>NOTE: This website is mainly for ANIME Torrents.</b>
>> Will get the Torrent details and their magnet link avaliable for the specified Search query.
"""

    print("Help requested!!!")
    return Msg