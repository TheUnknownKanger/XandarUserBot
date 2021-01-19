"""COMMAND : .gaay"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telebot.utils import admin_cmd
from telebot import CMD_HELP

@telebot.on(admin_cmd("gaay"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Abe Tu Gay tha Gay hai and Gay rhega and Tu Gand deta tha Gand deta hai and Tu Gandu Gand Deta rhega"
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

CMD_HELP.update( { "gaay": """**Plugin : dea Commands in degi are  • .da •  Function : **__Gali...__""" })
