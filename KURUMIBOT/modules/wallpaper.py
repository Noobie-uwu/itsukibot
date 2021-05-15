import os
from random import choice
from shutil import rmtree
from bing_image_downloader import downloader

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
    downloader.download(args)
    xx = choice(os.listdir(os.path.abspath(f"./resources/downloads/{query}/")))
    await event.client.send_file(event.chat_id, f"./resources/downloads/{query}/{xx}")
    rmtree(f"./resources/downloads/{query}/")
    await nn.delete()

