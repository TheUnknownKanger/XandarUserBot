"""Type `.poto` for get **All profile pics of that User**
\n Or type `.poto (number)` to get the **desired number of photo of a User** .
"""

import logging

from uniborg.util import admin_cmd

from telebot import CMD_HELP

logger = logging.getLogger(__name__)


if 1 == 1:
    name = "Profile Photos"
    client = borg

    @telebot.on(admin_cmd(pattern="poto(.*)"))
    @telebot.on(sudo_cmd(pattern="poto(.*)", allow_sudo=True))
    async def potocmd(event):
        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await borg.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await eor(event, "`ID number you entered is invalid`")
                    return
            except BaseException:
                await eor(event, "`Are you Comedy Me ?`")
                return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await borg.send_file(event.chat_id, send_photos)
            else:
                await eor(event, "`That user has no photos 🙄`")
                return


CMD_HELP.update(
    {
        "ppgrab": ".poto <a number (optional)> <reply to user>\nUse - get the persons profile pic(s)."
    }
)
