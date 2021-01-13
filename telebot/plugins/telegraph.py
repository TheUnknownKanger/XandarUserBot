"""@telegraph Utilities
Available Commands:
.telegraph media as reply to a media
.telegraph text as reply to a large text"""

import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from telebot.telebotConfig import Var

telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


@telebot.on(admin_cmd(pattern="telegraph (media|text) ?(.*)"))
@telebot.on(sudo_cmd(pattern="telegraph (media|text) ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    okey = await eor(event, "Scanning...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if Var.PRIVATE_GROUP_ID:
        await borg.send_message(
            Var.PRIVATE_GROUP_ID,
            "Created New Telegraph account {} for the current session. \n**Do not give this url to anyone, even if they say they are from Telegram!**".format(
                auth_url
            ),
        )
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        start = datetime.now()
        r_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str == "media":
            downloaded_file_name = await borg.download_media(
                r_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            await okey.edit(
                "Downloaded to {} in {} seconds.".format(downloaded_file_name, ms),
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await okey.edit("**Error : **" + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await okey.edit(
                    "Uploaded to this [Telegraph Page](https://telegra.ph{}) in {} seconds.".format(
                        media_urls[0], (ms + ms_two)
                    ),
                    link_preview=False,
                )
        elif input_str == "text":
            user_object = await borg.get_entity(r_message.from_id)
            title_of_page = user_object.first_name  # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                title_of_page = optional_title
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await borg.download_media(
                    r_message, Config.TMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(title_of_page, html_content=page_content)
            end = datetime.now()
            ms = (end - start).seconds
            link = f"https://telegra.ph/{response['path']}"
            await okey.edit(
                f"**link : ** [telegraph]({link})\
                 \n**Time Taken : **`{ms} seconds.`",
                link_preview=True,
            )
    else:
        await okey.edit(
            "`Reply to a message to get a permanent telegra.ph link. (Inspired by @ControllerBot)`",
        )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")
