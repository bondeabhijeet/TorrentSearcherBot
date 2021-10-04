


def BotHelpMessage(Commands):
    print(Commands)

    Msg = f"""
/{Commands['Help']}
>> Will get this message.

/{Commands['Yts']} <code>[ movie name ]</code> | <code>[ quality of the movie ]</code>
>> Will get the avaliable Direct Download Links of torrents for the specified movie name with mentioned quality
<b>NOTE: by default quality is 1080p.</b>"""

    print("Help requested!!!")
    return Msg