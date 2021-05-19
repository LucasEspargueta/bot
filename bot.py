import random
from discord.ext import commands
from pretty_help import PrettyHelp
import discord
import os
import time
from datetime import datetime
from pytz import timezone
import asyncio
import re

client = commands.Bot(command_prefix=['gimme '], help_command=PrettyHelp())
now = datetime.now(timezone('Europe/Lisbon'))
current_time = now.strftime("%H:%M:%S")

TIMEZONES = {
	"GMTM12": "Pacific/Auckland",
    "EST": "Etc/GMT+4",
    "GMT": "Etc/GMT",
    "PST": "Etc/GMT+7",
    "GMTM10": "Etc/GMT+10",
    "WET":'Europe/Lisbon',
    "GMTP13": "US/Samoa",
    "CST": "Etc/GMT+5",
    "TUGA": "Europe/Lisbon",
    "CET": "Europe/Madrid",
    "GMTM9": "Etc/GMT+9",
    "GMTM8": "US/Alaska",
    "GMTM7": "Etc/GMT+7",
    "GMTM6": "Etc/GMT+6",
    "GMTM5": "Etc/GMT+5",
    "GMTM4": "Etc/GMT+4",
    "GMTM3": "Etc/GMT+3",
    "GMTM2": "Etc/GMT+2",
    "GMTM1": "Etc/GMT+1",
    "GMTP2": "Europe/Madrid",
    "GMTP3": "Europe/Helsinki",
    "GMTP4": "Asia/Dubai",
    "GMTP5": "Asia/Karachi",
    "GMTP6": "Asia/Dhaka",
    "GMTP7": "Asia/Bangkok",
    "GMTP8": "Asia/Hong_Kong",
    "GMTP9": "Asia/Tokyo",
    "GMTP10": "Australia/Sydney",
    "GMTP11": "Asia/Magadan",
    "GMTP12": "Pacific/Auckland"
}

@client.event
async def on_ready():
    print('Vim-me!')

@client.command()
async def link(ctx):
    lista = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    await ctx.reply("https://prnt.sc/" + "".join(list(random.choices(lista, k=6))))
    
@client.command()
async def time(ctx, command="TUGA"):
    newtime = datetime.now(timezone(TIMEZONES[command.upper()])) if command.upper() in TIMEZONES.keys() else None

    if newtime:    
        current_time = newtime.strftime("%H:%M:%S")
        print(str(timezone), current_time)
        await ctx.reply(current_time)

@client.event
async def on_message(msg):
   if re.search(r"\btoni\b", msg.content, flags=re.I) is not None:
      await msg.reply("Tony")
   if "booba gif" in msg.content.lower():
       await msg.reply('https://i1.wp.com/media.tenor.com/images/3634fc2d789bdb041ec2d3088100ba7e/tenor.gif')
   if "big homies" in msg.content.lower():
      await msg.reply("https://cdn.discordapp.com/attachments/786571345072357376/843609641078620220/homies.png")
   if re.search(r"\bsimp\b", msg.content, flags=re.I) is not None:
      await msg.reply("https://cdn.discordapp.com/attachments/759903575748640798/843586394642317352/tEYCU9Ew.png")	
   if "ahegao gigante" in msg.content.lower():
      await msg.reply("https://cdn.discordapp.com/attachments/786571345072357376/842871472418193408/81376121441170228311.png")
   if "peraschamp" in msg.content.lower():
      await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/842518533888147486/unknown-2.jpg")
   if "letroll gigante" in msg.content.lower():
      await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/842824588042698762/IMG-20210505-WA0018_1.jpg")
   if msg.author == client.user:
      return
   if re.search(r"\bwoo+\b", msg.content, flags=re.I) is not None:
      await msg.reply("https://tenor.com/view/pop-smoke-dance-nyc-dance-move-smile-gif-16391422")
   if "this gigante" in msg.content.lower():
      await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/838739007415386112/this.png")
   if "among us" in msg.content.lower() or "amogus" in msg.content.lower():
      await msg.reply('among us')
   if "pedro ramalho" in msg.content.lower():
      await msg.reply('Pedro Ramalho \n https://cdn.discordapp.com/attachments/759882556744663040/818850186754785310/unknown.png')
   if "dababy" in msg.content.lower() or "less go" in msg.content.lower():
      await msg.reply("https://cdn.discordapp.com/attachments/379034825304178712/822505085820862494/IMG_20210318_233715.jpg")
   elif "balta" in msg.content.lower():
      num = random.randint(0, 100000)
      if num == 69420:
        await msg.reply('https://cdn.discordapp.com/attachments/759882556744663040/822255453677289482/SPOILER_unknown.png')
        print('racismo')
   await client.process_commands(msg)
@client.command()
async def cum(ctx):
   await ctx.reply('https://www.youtube.com/watch?v=uJ_1HMAGb4k')
@client.command()
async def gangnamstyle(ctx):
   await ctx.reply('https://www.youtube.com/watch?v=9bZkp7q19f0')
@client.command()
async def git(ctx):
   await ctx.reply('https://media.giphy.com/media/OOXp2e1gCnfj6jGxN9/giphy.gif')
    
client.run(os.environ["token"])
