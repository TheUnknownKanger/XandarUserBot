"""COMMAND : .da"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telebot.utils import admin_cmd
from telebot import CMD_HELP

@telebot.on(admin_cmd("da"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Ma Devil Hu Tera baap jisne teri ma chodi thi toh teri janam hua and fir tri bhenchod diya sale kabhi GT road pe jake de teri ma bhen free me gand dete hai wo ha and tere ma se pucha ki tera baap kon wo btae gi ki devil name hai tere baap and bhen se vu puchna sale ki isko kisne choda hai teri ma bhen dono chod diya randi bta kya kr lenga abh tu vi aja gand dede lund kela sala bsdka"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

CMD_HELP.update( { "da": """**Plugin : dea Commands in degi are  • .da •  Function : **__Gali By Devil...__""" })