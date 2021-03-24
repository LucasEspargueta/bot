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
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192',}]}
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([https://www.youtube.com/watch?v=1A_poY1VkKo])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    
    
async def hora():
    await asyncio.sleep(1)
    while True:
        now = datetime.now(timezone('UTC'))
        current_time = now.strftime("%H:%M:%S")
        await asyncio.sleep(1)
        if current_time == '23:34:00':
            canalvoz = client.get_channel(759884692219625493)
            canaltexto = client.get_channel(759882556744663040)
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
