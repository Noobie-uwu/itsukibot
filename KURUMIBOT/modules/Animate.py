import io
import json
import os
import random
import re
import emoji
from telethon import *
from telethon.tl import functions
from telethon.tl.types import *

from KURUMIBOT import *
from KURUMIBOT import TEMP_DOWNLOAD_DIRECTORY
from KURUMIBOT.events import register
from KURUMIBOT.ubot import ubot

@register(pattern="^/animate (.*)")
async def stickerizer(event):

    newtext = event.pattern_match.group(1)
    animus = [20, 32, 33, 40, 41, 42, 58]
    sticcers = await ubot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}"
    )
    null = await sticcers[0].download_media(TEMP_DOWNLOAD_DIRECTORY)
    bara = str(null)
    await event.client.send_file(event.chat_id, bara, reply_to=event.id)
    os.remove(bara)
