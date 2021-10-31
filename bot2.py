import random
from discord import message
from discord.ext import commands
from pretty_help import PrettyHelp
import discord
import os
import time
from datetime import datetime
from pytz import timezone
import asyncio
import re
import asyncpraw
import requests
import dicionarios

#reddit

reddit = asyncpraw.Reddit(client_id = "E7ja3WGqt2ToJA",
                     client_secret = os.environ['client_secret'],
                     username = "GriloDaFCUP",
                     password = os.environ['password'],
                     user_agent = "GriloDaFCUP 1.0 by /u/GriloDaFCUP")

# for time command
now = datetime.now(timezone('Europe/Lisbon'))
current_time = now.strftime("%H:%M:%S")

# important
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="gimme ", intents=intents)

# sexy help
color = int(''.join([random.choice('0123456789ABCDEF') for j in range(6)]), base=16)
client.help_command = PrettyHelp(color=color)

# rich presence
async def status():
    a = random.randint(1, 4)
    if a == 1:
        await client.change_presence(activity=discord.Game(name="Among Us"))
    if a == 2:
        await client.change_presence(
            activity=discord.Streaming(name="Cute animals", url='https://www.twitch.tv/marinemammalrescue'))
    if a == 3:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                               name="https://open.spotify.com/playlist/5RZQwNffu3pWAWiLc5yrfM"))
    if a == 4:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Cars"))
    await asyncio.sleep(0)


@client.event
async def on_ready():
    
    global guild
    guild = client.get_guild(int(759849368966004767))
    
    await status()


@client.slash_command(description="Gives you a random screenshot from the www, if you see anything inappropriate, please report it!"
,guild_ids=[655826315777146901,759849368966004767])
async def print(ctx):
    lista = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    await ctx.respond("https://prnt.sc/" + "".join(list(random.choices(lista, k=6))))


@client.slash_command(description='Gives you a random video from the www, if you see anything inappropriate, please report it!'
,guild_ids=[655826315777146901,759849368966004767])
async def video(ctx):
    lista = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    await ctx.respond("https://streamable.com/" + "".join(list(random.choices(lista, k=6))))


@client.slash_command(description='Gives you the time in different timezones. Try EST, PST, GMT, WET, CST & CET'
,guild_ids=[655826315777146901,759849368966004767])
async def time(ctx, command="TUGA"):
    newtime = datetime.now(timezone(dicionarios.TIMEZONES[command.upper()])) if command.upper() in dicionarios.TIMEZONES.keys() else None

    if newtime:
        current_time = newtime.strftime("%H:%M:%S")
        print(str(timezone), current_time)
        await ctx.respond(current_time)


@client.event
async def on_message(msg):
    m = msg.content.lower()
    if msg.author == client.user:
        return
    a = [dicionarios.EMOTES[s] for s in msg.content.split() if s in dicionarios.EMOTES]
    if a:
        await msg.channel.send("\n".join(a[:10]))
    if "booba gif" in msg.content.lower():
        await msg.reply('https://i1.wp.com/media.tenor.com/images/3634fc2d789bdb041ec2d3088100ba7e/tenor.gif')
    if "peras actually" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/851501480317026304/caption.png")
    if "big homies" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/786571345072357376/843609641078620220/homies.png")
    if re.search(r"\bsimp\b", msg.content, flags=re.I) is not None:
        await msg.reply("https://cdn.discordapp.com/attachments/759903575748640798/843586394642317352/tEYCU9Ew.png")
    if "ahegao gigante" in msg.content.lower():
        await msg.reply(
            "https://cdn.discordapp.com/attachments/786571345072357376/842871472418193408/81376121441170228311.png")
    if "peraschamp" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/842518533888147486/unknown-2.jpg")
    if "letroll gigante" in msg.content.lower():
        await msg.reply(
            "https://cdn.discordapp.com/attachments/759882556744663040/842824588042698762/IMG-20210505-WA0018_1.jpg")
    if "this gigante" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/838739007415386112/this.png")
    elif "balta" in msg.content.lower():
        num = random.randint(0, 100000)
        if num == 69420:
            await msg.reply(
                'https://cdn.discordapp.com/attachments/759882556744663040/822255453677289482/SPOILER_unknown.png')
            print('racismo')
    if m.startswith('[') and (
            msg.channel.name == '❓│1º_ano' or msg.channel.name == '❓│2º_ano' or msg.channel.name == '❓│3º-ano' or msg.channel.name == '❔│duvidas') and (
            ']' in m):
        vitrine = client.get_channel(853354421165228052)
        duvida = discord.Embed(title=msg.channel.name,
                               description='**' + msg.content + '** \n[Vê aqui](' + msg.jump_url + ') <a:leftarrow15:853378234405486593> <a:leftarrow15:853378234405486593>',
                               color=int(''.join([random.choice('0123456789ABCDEF') for j in range(6)]), base=16))
        if msg.attachments:
            image = msg.attachments[0].url
            duvida.set_image(url=image)
        duvida.set_footer(icon_url=msg.author.avatar_url,
                          text=f"Copia a pergunta para a barra de pesquisas para ver se já tem resposta! ")
        await vitrine.send(embed=duvida)
    await client.process_commands(msg)

@client.slash_command(description="PUSH TO THE GITHUB",guild_ids=[655826315777146901,759849368966004767])
async def git(ctx):
    await ctx.respond('https://media.giphy.com/media/OOXp2e1gCnfj6jGxN9/giphy.gif')

@client.slash_command(description="it's me",guild_ids=[655826315777146901,759849368966004767])
async def creator(ctx):
    await ctx.respond('https://github.com/LucasSexo/')

@client.slash_command(description="shows available emotes",guild_ids=[655826315777146901,759849368966004767])
async def emotes(ctx):
    emb = discord.Embed(title = "All available emotes", timestamp=datetime.utcnow(), description = ", ".join(dicionarios.EMOTES.keys()))
    emb.color = int(''.join([random.choice('0123456789ABCDEF') for j in range(6)]), base=16)
    await ctx.respond(embed = emb)

@client.slash_command(description = "sends nudes",guild_ids=[655826315777146901,759849368966004767])
async def nudes(ctx):
    subreddit = await reddit.subreddit("gonewild")
    all_subs = []

    top = subreddit.top("month", limit = 70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.utcnow())
    emb.set_image(url = url)
    emb.color = int(''.join([random.choice('0123456789ABCDEF') for j in range(6)]), base=16)

    await ctx.respond(embed = emb, ephemeral = True )
    print('O {} tá down bad'.format(ctx.author.name))
        
#desabafo stuff
@client.command()
async def anon(ctx, *, arg):
    if isinstance(ctx.channel, discord.channel.DMChannel):      #isto está aqui puramente 
        desabafo = client.get_channel(796509327997403156)       #por segurança e evitar spam
        print('O {} desabafou'.format(ctx.message.author.name)) #nao irei nunca divulgar quem usou o comando!
        desembed= discord.Embed(title="Anon says:", color= int(''.join([random.choice('0123456789ABCDEF') for j in range(6)]), base=16))
        desembed.description = arg
        
        await desabafo.send(embed = desembed)                                

vaccination_max_age, vaccination_last_updated = None, None

@client.slash_command(description='Sends a dm to a role (admin only)',guild_ids=[655826315777146901,759849368966004767])
async def comm(ctx, role: discord.Role, *, content):
    await ctx.defer()
    embed = discord.Embed(title="Comunicado Server FEUP ⚡ ", description=content, colour=0x423abc)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    if '832202769615552532' in str(ctx.author.id):
        for m in ctx.guild.members:
            if role in m.roles:
                await m.send(embed=embed)
        await ctx.respond("tá a dar (y)")
    else:
        await ctx.respond(ctx.author.mention + "you can't use that!")

client.run(os.environ["token"])
