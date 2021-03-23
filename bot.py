import os
import re
import random
from discord.ext import commands
import discord

client = commands.Bot(command_prefix=['cum '])
woo_regex = re.compile(r"woo+\b", flags=re.IGNORECASE)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Pedro Ramalho'))
      
@client.event
async def on_message(msg):
   if msg.author == client.user:
      return
   if woo_regex.search(msg.content) is not None:
      await msg.channel.send("https://tenor.com/view/pop-smoke-dance-nyc-dance-move-smile-gif-16391422")
   if "among us" in msg.content.lower() or "amogus" in msg.content.lower():
      await msg.channel.send('among us')
   if "pedro ramalho" in msg.content.lower():
      await msg.channel.send('Pedro Ramalho')
      await msg.channel.send('https://cdn.discordapp.com/attachments/759882556744663040/818850186754785310/unknown.png')
   elif "dababy" in msg.content.lower() or "less go" in msg.content.lower():
      await msg.channel.send("Let's go - DaBaby")
      await msg.channel.send('https://cdn.discordapp.com/attachments/379034825304178712/822505085820862494/IMG_20210318_233715.jpg')
   elif "balta" in msg.content.lower():
      num = random.randint(0, 1000000)
      if num == 69420:
        await msg.channel.send('https://cdn.discordapp.com/attachments/759882556744663040/822255453677289482/SPOILER_unknown.png')
   await client.process_commands(msg)

@client.command()
async def now(ctx):
   await ctx.send('https://www.youtube.com/watch?v=uJ_1HMAGb4k')

@client.command()
async def gangnamstyle(ctx):
   await ctx.send('https://www.youtube.com/watch?v=9bZkp7q19f0')

@client.command()
async def git(ctx):
   await ctx.send('https://media.giphy.com/media/OOXp2e1gCnfj6jGxN9/giphy.gif')

client.run(os.environ["token"])
