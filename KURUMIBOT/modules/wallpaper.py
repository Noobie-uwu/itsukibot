""" Wallpaper Module """

import os
import wget
import shutil
import requests

from pyrogram.types import InputMediaPhoto, InputMediaDocument
from PIL import Image

from KURUMIBOT.events import register


@register(pattern="^/wall ?(.*)")
async def wall(event):

    if os.path.exists("wallpapers/"):
        shutil.rmtree("wallpapers/", ignore_errors=True)

    limit = min(int(event.flags.get('-l', 8)), 10)

    if msg.filtered_input_str:
        qu = event.filtered_input_str
        await event.reply(f"`Seraching Wallpapers for {qu}`")
        results = requests.get(
            "https://api.unsplash.com/search/"
            f"photos?client_id=HWlOs9dNZIbYEkjp87fiEzC9rmE6rKM64tBqXBOLzu8&query={qu}"
        )

        if results.status_code != 200:
            return await msg.reply('**Result Not Found**')
        _json = results.json()['results']
        if len(_json) < limit:
            limit = len(_json)

        ss = []
        os.mkdir("wallpapers")

        for i in range(limit):
            img = f"wallpapers/wall_{i+1}.png"

            if '-doc' in msg.flags:
                await pool.run_in_thread(wget.download)(_json[i]['urls']['raw'], img)
                ss.append(InputMediaDocument(str(img)))
                continue

            await pool.run_in_thread(wget.download)(_json[i]['urls']['thumb'], img)
            image = Image.open(img)
            if not (image.height <= 1280 and image.width <= 1280):
                image.thumbnail((1280, 1280), Image.ANTIALIAS)
                a_dex = image.mode.find("A")
                if a_dex != -1:
                    new_im = Image.new('RGB', image.size, (255, 255, 255))
                    new_im.paste(image, mask=image.split()[a_dex])
                    new_im.save(img, 'JPEG', optimize=True)
            ss.append(InputMediaPhoto(str(img)))

        await event.reply_chat_action(
            "upload_photo" if '-doc' not in msg.flags else "upload_document")
        await event.reply_media_group(ss, True)
        shutil.rmtree("wallpapers/", ignore_errors=True)
        await event.delete()
    else:
        await event.reply('**Give me Something to search.**')
        await event.reply_sticker('CAADAQADmQADTusQR6fPCVZ3EhDoFgQ')
