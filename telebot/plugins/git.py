import asyncio

from telebot import CMD_HELP


@telebot.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "guthub":

        await eor(event, input_str)

        animation_chars = [
            "https://github.com/xditya/TeleBot",
            "https://github.com/spechide/UniBorg",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await eor(event, animation_chars[i % 2])


CMD_HELP.update({"git": ".guthub\nUse - Spam recents lol.."})
