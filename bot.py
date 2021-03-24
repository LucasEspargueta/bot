import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get
import os
from datetime import datetime
import time
from pytz import timezone
import asyncio

client = commands.Bot(command_prefix="!")

global voice
now = datetime.now(timezone('UTC'))

t = time.localtime()
global current_time



async def toca():

    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info('https://www.youtube.com/watch?v=1A_poY1VkKo', download=False)
        URL = info['formats'][0]['url']
    voice = get(client.voice_clients)
    voice.play(discord.FFmpegPCMAudio(URL))


async def hora():
    await asyncio.sleep(1)
    while True:
        now = datetime.now(timezone('UTC'))
        current_time = now.strftime("%H:%M:%S")
        await asyncio.sleep(1)
        if current_time == '18:41:10':
            canalvoz = client.get_channel(655826315777146909)
            canaltexto = client.get_channel(822774646981263360)
            await canaltexto.send('HORA DA ALTERNA :clock11: ')
            await canalvoz.connect()
            await asyncio.sleep(3)
            await toca()

@client.event
async def on_ready():
    print('on')
    await hora()
    
client.loop.create_task(hora())
client.run(os.environ["token"])
