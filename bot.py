import random
from discord.ext import commands
from pretty_help import PrettyHelp
import discord
import os

client = commands.Bot(command_prefix=['gimme '], help_command=PrettyHelp())
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
    await ctx.send("https://prnt.sc/" + "".join(list(random.choices(lista, k=6))))

@client.event
async def on_message(msg):
   if msg.author.id = 74434231882747904:
      await msg.channel.send("Tony")
   if msg.author == client.user:
      return
   if "woo" in msg.content.lower():
      await msg.channel.send("https://tenor.com/view/pop-smoke-dance-nyc-dance-move-smile-gif-16391422")
   if "among us" in msg.content.lower() or "amogus" in msg.content.lower():
      await msg.channel.send('among us', tts=True)
   if "pedro ramalho" in msg.content.lower():
      await msg.channel.send('Pedro Ramalho', tts=True)
      await msg.channel.send('https://cdn.discordapp.com/attachments/759882556744663040/818850186754785310/unknown.png')
   elif "dababy" in msg.content.lower() or "less go" in msg.content.lower():
      await msg.channel.send("Let's go - DaBaby", tts=True)
      await msg.channel.send('https://cdn.discordapp.com/attachments/379034825304178712/822505085820862494/IMG_20210318_233715.jpg')
   elif "balta" in msg.content.lower():
      num = random.randint(0, 1000000)
      if num == 69420:
        await msg.channel.send('https://cdn.discordapp.com/attachments/759882556744663040/822255453677289482/SPOILER_unknown.png')
        print('racismo')
   await client.process_commands(msg)
@client.command()
async def cum(ctx):
   await ctx.send('https://www.youtube.com/watch?v=uJ_1HMAGb4k')
@client.command()
async def gangnamstyle(ctx):
   await ctx.send('https://www.youtube.com/watch?v=9bZkp7q19f0')
@client.command()
async def git(ctx):
   await ctx.send('https://media.giphy.com/media/OOXp2e1gCnfj6jGxN9/giphy.gif')
    
client.run(os.environ["token"])
