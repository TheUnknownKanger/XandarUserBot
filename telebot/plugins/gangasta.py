import asyncio

from telebot import CMD_HELP
from telebot.utils import admin_cmd


@telebot.on(admin_cmd(pattern="gangasta ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("EVERyBOdy")
        await asyncio.sleep(0.3)
        await event.edit("iZ")
        await asyncio.sleep(0.2)
        await event.edit("GangSTur")
        await asyncio.sleep(0.5)
        await event.edit("UNtIL ")
        await asyncio.sleep(0.2)
        await event.edit("I")
        await asyncio.sleep(0.3)
        await event.edit("ArRivE")
        await asyncio.sleep(0.3)
        await event.edit("🔥🔥🔥")
        await asyncio.sleep(0.3)
        await event.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥🔥🔥")


CMD_HELP.update({"gangsta": ".gangsta\nUse - Spam recents of a group lel."})
