#Officially By Devil
"""Emoji
Available Commands:
.devil"""

from telethon import events

import asyncio

from telebot import CMD_HELP
from telebot.utils import admin_cmd

@telebot.on(admin_cmd("devil"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "gulli":
    await event.edit("gulli")
    animation_chars = [
            "OK",
            "I am Devil",
            "Jisne teri Gand mara tha wo devil hu",
            "Agr Tum Hellbot User Ho",
            "Not Forgot Devil Iz King Of Hell",
            "So Devilbot User is king of Hellbot",
            "Abh tu gandu",
            "Nikal yaha se",
            "Fir mat kehna Gand fat giyi agr teri",
            "SAMJHAA LAWDE",
            "YA DU TERE GAAND ME TAPAA TAP😂",
            "TERI BEHEN MERA ROZ LETI HAI",
            "TERI GF K SAATH MMS BANAA CHUKA HU🙈🤣🤣",
            "TU CHUTIYA TERA KHANDAAN CHUTIYA",
            "Yeahhhhhh",
            "AUR KITNA BOLU BEY MANN BHAR GAYA MERA🤣",
            "Ab nikal ja jaake chkko k saath hilaa",
            "😂😂😂🤣🤣"
        ]

    for i in animation_ttl:
         
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

CMD_HELP.update({
    "devil":"Use And Check.devil"})
