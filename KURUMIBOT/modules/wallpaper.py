import os
from random import choice
from shutil import rmtree
import google_images_download.google_images_download as gi

from KURUMIBOT.events import register

@register(pattern="^/wall ?(.*)")
async def wall(event):
    inp = event.pattern_match.group(1)
    if not inp:
        return await event.reply("Please enter a query!")
    nn = await event.reply("Processing Keep Patience...")
    query = f"hd {inp}"
    args = {
        "keywords": query,
        "limit": 10,
        "format": "jpg",
        "output_directory": "./resources/downloads/",
    }
    gi.download(args)
    xx = choice(os.listdir(os.path.abspath(f"./resources/downloads/{query}/")))
    await event.client.send_file(event.chat_id, f"./resources/downloads/{query}/{xx}")
    rmtree(f"./resources/downloads/{query}/")
    await nn.delete()

