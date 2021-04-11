import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get
import os
from datetime import datetime
import time
from pytz import timezone
import asyncio
import random
from pretty_help import PrettyHelp
import re

client = commands.Bot(command_prefix=['gimme '], help_command=PrettyHelp())
woo_regex = re.compile(r"woo+\b", flags=re.IGNORECASE)
global voice
now = datetime.now(timezone('Europe/Lisbon'))
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
        now = datetime.now(timezone('Europe/Lisbon'))
        current_time = now.strftime("%H:%M:%S")
        await asyncio.sleep(1)
        if current_time == '23:15:00':
            canalvoz = client.get_channel(759880326985154600)
            canaltexto = client.get_channel(759882556744663040)
            await asyncio.sleep(1)
            await canaltexto.send(':clock11: HORA DA ALTERNA :clock11: \n' 'https://cdn.discordapp.com/attachments/759882556744663040/824573836468158484/booba.png')
            await canalvoz.connect()
            await asyncio.sleep(1)
            await toca()
            print("Hora da alterna começou")

@client.event
async def on_ready():
    print('on')
    await hora()

@client.command(name="link", help="Generates a random Lightshot link")
async def link(ctx):
    lista = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    print("Link criado")
    await ctx.send("Caso contenha algo inadequado, por favor reporta abrindo o link.\n" "https://prnt.sc/" + "".join(list(random.choices(lista, k=6))))

client.loop.create_task(hora())
client.run(os.environ["token"])
