"""Dictionary Plugin for @UniBorg
Syntax: .meaning <word>"""

import requests
from uniborg.util import admin_cmd

from telebot import CMD_HELP


@telebot.on(admin_cmd(pattern="meaning (.*)"))
@telebot.on(sudo_cmd(pattern="meaning (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    input_url = "https://bots.shrimadhavuk.me/dictionary/?s={}".format(input_str)
    headers = {"USER-AGENT": "UniBorg"}
    caption_str = f"Meaning of __{input_str}__\n"
    try:
        response = requests.get(input_url, headers=headers).json()
        pronounciation = response.get("p")
        meaning_dict = response.get("lwo")
        for current_meaning in meaning_dict:
            current_meaning_type = current_meaning.get("type")
            current_meaning_definition = current_meaning.get("definition")
            caption_str += (
                f"**{current_meaning_type}**: {current_meaning_definition}\n\n"
            )
    except Exception as e:
        caption_str = str(e)
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:
        await borg.send_file(
            event.chat_id,
            pronounciation,
            caption=f"Pronounciation of __{input_str}__",
            force_document=False,
            reply_to=reply_msg_id,
            allow_cache=True,
            voice_note=True,
            silent=True,
            supports_streaming=True,
        )
    except BaseException:
        pass
    await eor(event, caption_str)


CMD_HELP.update({"dictionary": ".meaning <word>\nUse - Get the meaning of that word."})
