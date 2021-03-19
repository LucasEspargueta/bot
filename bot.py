import os
from discord.ext import commands

client = commands.Bot(command_prefix=['cum '])

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Miauuu'))
      
@client.event
async def on_message(msg):
   if msg.author == client.user:
      return
   if "pedro ramalho" in msg.content.lower():
      await msg.channel.send('Pedro Ramalho')
   elif   "dababy" in msg.content.lower():
      await msg.channel.send('DaBaby')
   elif   "less go" in msg.content.lower():
      await msg.channel.send('https://cdn.discordapp.com/attachments/379034825304178712/822505085820862494/IMG_20210318_233715.jpg')
   elif   "balta" in msg.content.lower():
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
