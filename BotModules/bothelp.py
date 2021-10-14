


def BotHelpMessage(Commands):
    print(Commands)

    Msg = f"""
/{Commands['Help']}
>> Will get this message.

/{Commands['Yts']} <code>[ movie name ]</code> | <code>[ quality of the movie ]</code>
>> Will get the Direct Download Links of torrents avaliable for the specified movie name with mentioned quality
<b>NOTE: by default quality is 1080p.</b>

/{Commands['o1337x']} <code>[ Search query ]
>> Will get the Torrent details and their magnet link avaliable for the specified Search query
"""

    print("Help requested!!!")
    return Msg